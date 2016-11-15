# Implementation of Single Linked List


# Define the Node for linked list
class ListNode:
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return (self._data)

def main():
    # Adding the nodes
    node1 = ListNode('Name')
    node2 = ListNode('Kemal')
    node3 = ListNode('Ergin')
    node4 = ListNode('Enes')
    #node5 = node3

    # Linking the nodes to make a linked list
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    #node5.next = None


    traversal(node1)
    # if unorderedSearch(node1, 'Enes'):
    #     print("Enes is in linked list")

# Traversing a linked list
def traversal(head):
    curNode = head
    while curNode is not None:
        print curNode
        curNode = curNode.next

# Searching a linked list
def unorderedSearch(head, target):
    curNode = head
    while curNode is not None and curNode != target:
        curNode = curNode.next

    return curNode is not None

if __name__ == '__main__':
    main()
