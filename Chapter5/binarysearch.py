# Implementation of Binary Search algorithm

import random

def main():
    _list = random.sample(xrange(1, 101), 10)
    value = 87
    print("Searching for the value: " + str(value))
    if binarySearch(value):
        print("The number " + str(value) + " found in the list")
    else:
        print("The number " + str(value) + " not found in the list")

def binarySearch(theValues, target):
    # Start with the entire sequence of elements. 0:length
    low = 0
    high = len(theValues - 1)

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
        # Or does the target precede the midpoint?
        elif target < theValues[mid]:
            high = mid - 1 # Update the upper bound

        # Or does it follow the midpoint
        else:
            low = mid + 1 # Update the lower bound

    # If the sequence cannot be subdivided further, we're done.
    return False


if __name__ == '__main__':
    main()
