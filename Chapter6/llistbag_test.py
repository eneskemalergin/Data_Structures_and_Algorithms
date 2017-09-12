# Testing script for linked list implementation of Bag ADT
from llistbag import Bag

def main():
    print("Testing class constructor:")
    LLBag = Bag()

    print("Testing add method:")
    LLBag.add(45)
    LLBag.add(25)
    LLBag.add(52)
    LLBag.add(17)

    print("Testing in method:")
    print(45 in LLBag)

    print("Testing iteration method:")
    for i in LLBag:
        print(i)

    print("Testing remove method:")
    LLBag.remove(17)
    LLBag.remove(18)

if __name__ == '__main__':
    main()
