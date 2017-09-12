# Implementation of Bag ADT using Singly Linked List

class Bag:
    # Construct an empty bag
    def __init__(self):
        self._head = None
        self._size = 0

    # Return the number of items in the bag.
    def __len__(self):
        return self._size

    # Determine if an item is contained in the bag.
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

    # Add a new item to the bag
    def add(self, item):
        # TODO: Review here if I could use the Node class
        newNode = _BagListNode(item) # Takes advantage of private storage class
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    # Remove an instance of the item from the bag
    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        # Check if item is even in the list otherwise return error
        assert curNode is not None, "The item must be in the bag."

        # Unlink the node and return the item.
        self._size -= 1
        if curNode is head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item

    # Return the iterator for traversing the list of items.
    def __iter__(self):
        return _BagIterator(self._head)

# Define a private storage class for creating list nodes.
class _BagListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# Define a linked list iterator for the Bag ADT
class _BagIterator:
    def __init__(self, listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
