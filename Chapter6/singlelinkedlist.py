# Implementation of Singly Linked List using Node Class

from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head == None :
			self.head = newNode
		else :
			newNode.next = self.head
			newNode.next.prev = newNode
			self.head = newNode

    def traversal(self, head):
        curNode = head
        while curNode is not None:
            pass
        pass

    def unorderedSearch(self, target):
        curNode = self.head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None
