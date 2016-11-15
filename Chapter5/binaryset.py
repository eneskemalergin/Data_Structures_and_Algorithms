# Implementation of the Set ADT using a sorted list.

class Set:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(self) and self._theElements[ndx] == element

    # Adds a new unique element to the set
    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)

    # Determines if this set is a subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True

    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0
        # Merge the two lists together until one is empty.
        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueb = setB._theElements[b]

            if valueA < valueB:
                newSet._theElements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1
            # Only one of the two duplicates are appended
            else:
                newSet._theElements.append(valueA)
                a += 1
                b += 1

        # If a listA contains more items, append them to newList.
        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1

        # Or if listB contains more items, append them to newList.
        while b < len(setB):
            newSet._theElements.append(setB._theElements[b])
            b += 1

        return newSet

    def difference(self, setB):
        newSet = Set()
        a = 0
        b = 0


    def intersect(self, setB):
        newSet = Set()
        a = 0
        b = 0

    # def isSubsetOf(self, setB):
    #     newSet

    def __add__(self, setB):
        return self.union()

    def __sub__(self, setB):
        return self.difference()

    def __mul__(self):
        return self.intersect()


    def __iter__(self):
        return _SetIterator(self._theElements)

    def _findPosition(self, element):
        low = 0
        high = len(theList) - 1
        while low <= high:
            mid = (high - low) / 2
            if theList[mid] == target:
                return mid
            elif target < theList[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low

# Iterator class for set __iter__
class _SetIterator:
    def __init__( self, theList ):
        self._setItems = theList
        self._curNdx = 0

    def __iter__( self ):
        return self

    def next( self ):
        if self._curNdx < len( self._setItems ):
            item = self._setItems[ self._curNdx ]
            self._curNdx += 1
            return item
        else:
            raise StopIteration
