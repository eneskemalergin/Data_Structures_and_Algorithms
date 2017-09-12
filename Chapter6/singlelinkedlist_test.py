# Testing script to see every method and the class itself is functional
from singlelinkedlist import SinglyLinkedList

def main():
    print("Testing class constructor:")
    SLL = SinglyLinkedList()

    print("Testing add method:")
    SLL.add(45)
    SLL.add(25)
    SLL.add(52)
    SLL.add(17)

    print("Testing traversal method:")
    SLL.traversal()

    print("Testing unorderedSearch method:")
    SLL.unorderedSearch(52)

    print("Testing remove method:")
    SLL.remove(17)


if __name__ == '__main__':
    main()
