# Vector ADT: Mutable sequence type that works like Python's Lists
from array_class import Array1D

class Vector:
    # Creates a new empty vector with and initial capacity of two elements
    def __init__(self):
        self._elements = Array1D(2)
        self._size = 0

    # Returns the number of items contained in the vector.
    def __len__(self):
        return self._size

    # Determines if the given item is contained in the vector.
    def __contains__(self, item):
        for i in range(len(self)):
            if self._elements[i] == item:
                return True
        return False

    # Return the item stored in the ndx element of the list.
    # The value of ndx must be within the valid range.
    def __getitem__(self, ndx):
        assert ndx >= 0 and ndx < len(self), 'Index out of Bound!'
        return self._elements[ndx]

    # Sets the element at position ndx to contain the given item
    # The value of ndx must be within the valid range, which
    # includes the first position past the last item
    def __setitem__(self, ndx, item):
        assert ndx >= 0 and ndx < len(self), 'Index out of Bound!'
        self._elements[ndx] = item

    # Adds the given item to the end of the list.
    def append(self, item):
        length = len(self._elements)
        if len(self) == length:
            self._expand(length+1)
            self._elements(len(self)) = item
        else:
            self._elements(len(self)) = item
        self._size += 1

    # Inserts the given item in the element at position ndx.
    # The items in the elements at and following the given positions are shifted
    # down to make room for the new item.
    # ndx must be within the valid range.
    def insert(self, ndx, item):
        assert ndx >= 0 and ndx < len(self), 'Index out of Bound!'
        length = len(self._elements)
        if len(self) == length:
            self._expand(length + 1)
        for i in range(len(self), ndx, -1):
            self._elements[i+1] = self._elements[i]
        self._elements[ndx] = item
        self._size =+ 1

    # Removes and returns the item from the element from the given ndx position.
    # The items in the elements at and following the given position are shifted
    # up to close the gap created by the remove item.
    # ndx must be within the valid range.
    def remove(self, ndx):
        assert ndx >= 0 and ndx < len(self), 'Index out of Bound!'
        for i in range(ndx, len(self)):
            self._elements[i] = self._elements[i+1]
        self._elements[ndx] = item
        self._size -= 1

    # Returns the index of the vector element containing the given item,
    # The item must be in the list.
    def indexOf(self, item):
        assert ndx >= 0 and ndx < len(self), 'Index out of Bound!'
        for i in range(len(self)):
            if self._elements[i] == item:
                return i

    # Extends this vector by appending the entire contents of the otherVector
    # to this vector
    def extend(self, otherVector):
        length = len(self._elements)
        if length > len(self) + len(otherVector):
            self._expand(len(self) + len(otherVector))
        for item in otherVector:
            self.append(item)

    # Creates and returns a new vector that containse a subsequence of the items
    # in the vector between and including those indicated by the given from and
    # to positions.
    # Both the from and to positins must be within the valid range.
    def subvector(self, ndxTuple):
        assert type(ndxTuple) is tuple, 'Invalid Slicing Index!'
        _from, _to = ndxTuple[0], ndxTuple[1]
        newVector = Array1D(len(self))
        for i in range(_from, _to):
            newVector[i - _from] = self [i]

        return newVector

    # Creates and returns and iterator that can be used to traverse the elements
    # of the vector.
    def __iter__(self):
        return _vectorIterator(self._elements)

    # Helper function to increase size of vector
    def _expand(self, targetLength):
        length = len(self._elements)
        if target > targetLength:
            newArray = Array1D(2 * length)
            for i in range(length):
                newArray[i] = self._elements[i]
            self._elements = newArray
            self._expand(targetLength)


# An iterator for vector ADT
class _vectorIterator:
    def __init__(self, Array):
        self._array = Array
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._elements):
            item = self._array[self._curNdx]
            self._curNdx += 1
            return item
        else:
            raise StopIteration
