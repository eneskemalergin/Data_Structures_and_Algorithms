# Implementation of Singly Linked List using Node Class
# TODO: Very Buggy Implementation, check the add method
# REVIEW: Review the concept

from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def checkOrder(self):
        """Checks if linked list is ordered or not:
         Returns Boolean"""
        pass

    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            newNode.next.prev = newNode
            self.head = newNode

    def traversal(self):
        curNode = self.head
        while curNode is not None:
            print(curNode)
            curNode = curNode.next

    def unorderedSearch(self, target):
        curNode = self.head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    def orderedSearch(self, target):
        """Searches the target on the linked lists:
        """
        if order != None: # If the checkOrder function is ran and we have order variable
            if order == True:
                # Complete the method
                pass
            else:
                print("orderedSearch is cannot be done in unordered Linked List")
        else: # If we did not check the Order yet,
            order = checkOrder()
            if order == True:
                # Complete the method
                pass
            else:
                print("orderedSearch is cannot be done in unordered Linked List")

    def remove(self, target):
        predNode = None
        curNode = self.head
        while curNode is not None and curNode.data != target:
            predNode = curNode
            curNode = curNode.next

        if curNode is not None:
            if curNode is self.head:
                self.head = curNode.next
            else:
                predNode.next = curNode.next

    def __str__( self ):
        # Simplfied printing by adding all the elements to string
        s = ""
        curNode = self.head
        if curNode != None :
            while curNode.next != None :
                s += curNode.data
                curNode = curNode.next
            s += curNode.data
        return ' '.join(list(s))
