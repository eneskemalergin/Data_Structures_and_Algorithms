# Implementation of 2 sorted list merging
# The lists should be sorted before hand

import random

def main():
    _listA = range(1,40,5)
    _listB = range(1,40,8)
    print("List 1: ", _listA)
    print("List 2: ", _listB)
    print("Merged and Sorted List: ")
    print(mergeSortedLists(_listA, _listB))

# Merges two sorted list to create and return a new sorted list.
def mergeSortedLists(listA, listB):
    # Create a new list and initialize the list markers
    newList = list()
    a = 0
    b = 0

    # Merge the two lists together until one is empty.
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    # If listA contains more items, append them to newList
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    # Or if listB contains more items, append them to newList
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList


if __name__ == '__main__':
    main()
