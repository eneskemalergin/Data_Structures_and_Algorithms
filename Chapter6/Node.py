# Implementation of Node for the Linked List Classes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def iter(self):
        node = self
        while True:
            yield node.value

            if node.next:
                node = node.next
            else:
                raise StopIteration()

    
