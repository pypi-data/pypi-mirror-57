from collections.abc import MutableSet
from functools import singledispatch
import typing as t

SliceAll = slice(None)
generator = type(e for e in ())


def sget(target, key: str, default: t.Any = None):
    """
    structure-get, a function simmilar to dict's 'get' method, which can resolve inner
    structure of keys. A string-typed key may be composed of series of keys (for maps)
    or indexes (for sequences), concatenated with dots. The method cat take a default value,
    just as dict.get does.

    An example:
    >>> bunch = Bunch(foo={'bar': ['value']})
    >>> assert sget(bunch, 'foo.bar.0') == 'value'
    >>> assert sget(bunch, 'foo.baz', 42) == 42
    """
    key_iter = key.split('.') if hasattr(key, 'split') else [key]
    value = target
    for part in key_iter:
        try:
            # attribute access
            value = getattr(value, part)
        except (TypeError, AttributeError):
            try:
                # key access
                value = value[part]
            except (TypeError, KeyError):
                # index access
                try:
                    value = value[int(part)]
                except (TypeError, ValueError, IndexError, KeyError):
                    return default
    return value


@singledispatch
def freeze(obj):
    """Returns immutable copy of the `obj`"""
    return obj


@freeze.register(dict)
def _(d: dict):
    return frozendict((k, freeze(v)) for k, v in d.items())


@freeze.register(list)
def _(l: list):
    return tuple(freeze(v) for v in l)


@freeze.register(set)
def _(s: set):
    return frozenset(freeze(v) for v in s)


def is_iterable(obj):
    """
    Are we being asked to look up a list of things, instead of a single thing?
    We check for the `__iter__` attribute so that this can cover types that
    don't have to be known by this module, such as NumPy arrays.
    Strings, however, should be considered as atomic values to look up, not
    iterables.
    We don't need to check for the Python 2 `unicode` type, because it doesn't
    have an `__iter__` attribute anyway.
    """
    return hasattr(obj, '__iter__') and not isinstance(obj, str)


def is_iterable_and_not_tuple(obj):
    """
    As in `is_iterable` with one addition:
    the same goes for tuples, since they are immutable and therefore
    are valid entries for indexes.
    """
    return is_iterable(obj) and not isinstance(obj, tuple)


class OrderedSet(MutableSet):
    """
    An OrderedSet is a custom MutableSet that remembers its order, so that
    every entry has an index that can be looked up.

    The code and its tests are taken from:
    https://github.com/LuminosoInsight/ordered-set
    """
    def __init__(self, iterable=None):
        self.items = []
        self.map = {}
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        """
        Get the item at a given index.
        If `index` is a slice, you will get back that slice of items. If it's
        the slice [:], exactly the same object is returned. (If you want an
        independent copy of an OrderedSet, use `OrderedSet.copy()`.)
        If `index` is an iterable, you'll get the OrderedSet of items
        corresponding to those indices. This is similar to NumPy's
        "fancy indexing".
        """
        if index == SliceAll:
            return self
        elif hasattr(index, '__index__') or isinstance(index, slice):
            result = self.items[index]
            if isinstance(result, list):
                return OrderedSet(result)
            else:
                return result
        elif is_iterable_and_not_tuple(index):
            return OrderedSet([self.items[i] for i in index])
        else:  # pragma: no cover
            raise TypeError(
                "Don't know how to index an OrderedSet by %r" % index)

    def copy(self):
        return OrderedSet(self)

    def __getstate__(self):
        if len(self) == 0:
            # The state can't be an empty list.
            # We need to return a truthy value, or else __setstate__
            # won't be run.
            #
            # This could have been done more gracefully by always putting
            # the state in a tuple, but this way is backwards- and forwards-
            # compatible with previous versions of OrderedSet.
            return (None,)
        else:
            return list(self)

    def __setstate__(self, state):
        if state == (None,):
            self.__init__([])
        else:
            self.__init__(state)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        """
        Add `key` as an item to this OrderedSet, then return its index.
        If `key` is already in the OrderedSet, return the index it already
        had.
        """
        if key not in self.map:
            self.map[key] = len(self.items)
            self.items.append(key)
        return self.map[key]
    append = add

    def update(self, sequence):
        """
        Update the set with the given iterable sequence, then return the index
        of the last element inserted.
        """
        item_index = None
        try:
            for item in sequence:
                item_index = self.add(item)
        except TypeError:  # pragma: no cover
            raise ValueError(
                'Argument needs to be an iterable, got %s' % type(sequence))
        return item_index

    def index(self, key):
        """
        Get the index of a given entry, raising an IndexError if it's not
        present.
        `key` can be an iterable of entries that is not a string, in which case
        this returns a list of indices.
        """
        if is_iterable_and_not_tuple(key):
            return [self.index(subkey) for subkey in key]
        return self.map[key]

    def pop(self):
        """
        Remove and return the last element from the set.

        Raises KeyError if the set is empty.
        """
        if not self.items:
            raise KeyError('Set is empty')

        elem = self.items[-1]
        del self.items[-1]
        del self.map[elem]
        return elem

    def discard(self, key):
        """
        Remove an element.  Do not raise an exception if absent.
        The MutableSet mixin uses this to implement the .remove() method, which
        *does* raise an error when asked to remove a non-existent item.
        """
        if key in self:
            i = self.items.index(key)
            del self.items[i]
            del self.map[key]
            for k, v in self.map.items():
                if v >= i:
                    self.map[k] = v - 1

    def clear(self):
        """
        Remove all items from this OrderedSet.
        """
        del self.items[:]
        self.map.clear()

    def __iter__(self):
        return iter(self.items)

    def __reversed__(self):
        return reversed(self.items)

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and self.items == other.items
        try:
            other_as_set = set(other)
        except TypeError:
            # If `other` can't be converted into a set, it's not equal.
            return False
        else:
            return set(self) == other_as_set


def get_duplicates(iterable):
    """
    Returns set of duplicated items from iterable. Item is duplicated if it
    appears at least two times.
    """
    seen = set()
    seen2 = set()
    for item in iterable:
        if item in seen:
            seen2.add(item)
        else:
            seen.add(item)
    return seen2


@singledispatch
def iterate_over_values(collection):
    yield collection


@iterate_over_values.register(list)
@iterate_over_values.register(tuple)
@iterate_over_values.register(set)
@iterate_over_values.register(OrderedSet)
def _(collection):
    for value in collection:
        yield from iterate_over_values(value)


@iterate_over_values.register(dict)
def _(collection):
    for key in sorted(collection):
        yield from iterate_over_values(collection[key])


# noinspection PyPep8Naming
class frozendict(dict):  # noqa: N801
    """
    Frozen (immutable) version of dict. Name is left to be consistent with
    set/frozenset pair.

    The code is taken from:
    code.activestate.com/recipes/414283-frozen-dictionaries/
    """

    def __not_implemented__(self, *args, **kwargs):
        raise AttributeError("A frozendict cannot be modified.")

    __delitem__ = __setitem__ = clear = \
        pop = popitem = setdefault = update = __not_implemented__

    def __copy__(self):
        """
        Addresses the problem with copy.copy(frozendict()) and its default copier (which asserts
        mutability of the target).
        """
        return frozendict(dict.copy(self))

    def __new__(cls, *args, **kwargs):
        new = dict.__new__(cls)
        combined_kwargs = {}
        for structure in args + (kwargs,):
            if isinstance(structure, (list, generator)):
                combined_kwargs.update({v0: v1 for v0, v1 in structure})
            elif isinstance(structure, dict):
                combined_kwargs.update(structure)
        frozen_structure = [(freeze(k), freeze(v)) for k, v in combined_kwargs.items()]
        dict.__init__(new, frozen_structure)
        return new

    def __hash__(self):
        try:
            return self._cached_hash
        except AttributeError:
            self._cached_hash = hash(frozenset(self.items()))
            return self._cached_hash

    def __repr__(self):
        return "frozendict(%s)" % dict.__repr__(self)


class Bunch(dict):
    """
    Dict-like object which gives attribute access to its components.

    An example:
    >>> bunch = Bunch(foo='bar')
    >>> assert bunch.foo == 'bar'
    >>> bunch.foo = {'bar': ['baz']}
    >>> assert bunch['foo'] = {'bar': ['baz']}
    """

    def __getattr__(self, key: str) -> t.Any:
        """
        Gets key if it exists, otherwise throws AttributeError.
        NB __getattr__ is only called if key is not found in normal places.

        :raises: AttributeError
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key: str, value: t.Any) -> None:
        """
        Sets value under the specified key. Translates TypeError
        (ie. unhashable keys) to AttributeError.

        :raises: AttributeError
        """
        try:
            self[key] = value
        except (KeyError, TypeError):
            raise AttributeError(key)

    def __delattr__(self, key: str) -> None:
        """
        Deletes attribute k if it exists, otherwise deletes key k. A KeyError
        raised by deleting the key--such as when the key is missing--will
        propagate as an AttributeError instead.

        :raises: AttributeError
        """
        try:
            del self[key]
        except KeyError:
            raise AttributeError(key)

    def __repr__(self) -> str:
        """
        Invertible string-form of a Bunch.
        """
        keys = list(self.keys())
        keys.sort()
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(['%s=%r' % (key, self[key]) for key in keys])
        )
