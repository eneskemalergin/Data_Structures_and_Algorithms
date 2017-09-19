# Implementation of Node for the Linked List Classes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def iter(self):
        node = self
        while True:
            yield node.value
            if node.next:
                node = node.next
            else:
                raise StopIteration()
