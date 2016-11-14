# Implementation of insertion sort algorithm

import random

def main():
    _list = random.sample(xrange(1, 101), 10)
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
