# Implementation of bubble sort algorithm

import random

def generateTest(length):
    return random.sample(xrange(1, 101), length)


def main():
    given_list = [80,7,24,16,43,91,35,2,19,72]
    print("Given Randomized list: ", given_list)
    print("Sorted List: ", bubbleSort(given_list))

    for _ in range(1):
        _list = generateTest(5)
        print("Randomized list: ", _list)
        print("Sorted List: ", bubbleSort(_list))

# Sorts a sequence in ascending order using the bubble sort algorith.
def bubbleSort(seq):
    not_sorted = True
    n = len(seq)
    # print "At the beginning: "
    # print seq
    while not_sorted:
        # If following statements fail next statement will stop the loop
        not_sorted = False
        for i in range(n-1):
            if seq[i] <= seq[i+1]:
                continue;
            else:
                temp = seq[i]
                seq[i] = seq[i+1]
                seq[i+1] = temp

            not_sorted = True
            # print seq
    return seq


if __name__ == '__main__':
    main()
