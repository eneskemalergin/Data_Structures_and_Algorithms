# Implementation of selection sort algorithm

import random

def generateTest(length):
    return random.sample(xrange(1, 101), length)


def main():
    given_list = [80,7,24,16,43,91,35,2,19,72]
    print("Given Randomized list: ", given_list)
    print("Sorted List: ", selectionSort(given_list))

    for _ in range(1):
        _list = generateTest(5)
        print("Randomized list: ", _list)
        print("Sorted List: ", selectionSort(_list))

# Sorts a sequence in ascending order using the selection sort algorithm
def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        # Assume the ith element is the smallest.
        smallNdx = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        # Swap the ith value and smallNdx value only if the smallest value is
        # not really in its proper position. Some implementations omit testing
        # the condition and always swap the two values.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

    return theSeq


if __name__ == '__main__':
    main()
