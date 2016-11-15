# Implementation of insertion sort algorithm

import random

def generateTest(length):
    return random.sample(xrange(1, 101), length)


def main():
    given_list = [80,7,24,16,43,91,35,2,19,72]
    print("Given Randomized list: ", given_list)
    print("Sorted List: ", insertionSort(given_list))

    for _ in range(1):
        _list = generateTest(5)
        print("Randomized list: ", _list)
        print("Sorted List: ", insertionSort(_list))

# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned.
        value = theSeq[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the rigth during search
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

        theSeq[pos] = value
    return theSeq


if __name__ == '__main__':
    main()
