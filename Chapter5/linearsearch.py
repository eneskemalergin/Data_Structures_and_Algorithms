# Implementation of linearsearch functions.

import random

def main():

    _list = random.sample(xrange(1, 101), 10)
    print("Finding Smallest number, " +  str(findSmallest(_list)))
    print("Finding Biggest number, " + str(findBiggest(_list)))

def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        # If the target is in the ith element, return True
        if theValues[i] == target:
            return True
    # If not found, return False.
    return False

def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):
        # If the target is found in the ith element, return True
        if theValues[i] == item:
            return True
        # If target is largers than the ith element, it's not in the sequence.
        elif theValues[i] > item:
            return False

    # The item is not in the sequence.
    return False

def findSmallest(theValues):
    n = len(theValues)
    # Assume the first item is the smallest value
    smallest = theValues[0]
    # Determine if any other item in the sequence is smaller.
    for i in range(1,n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    # Return the smallest found.
    return smallest

def findBiggest(theValues):
    n = len(theValues)
    # Assuming the first item is the biggest value
    biggest = theValues[0]
    # Determine if any other item in the sequence is bigger.
    for i in range(1, n):
        if theValues[i] > biggest:
            biggest = theValues[i]
    #Return the biggest found.
    return biggest


if __name__ == '__main__':
    main()
