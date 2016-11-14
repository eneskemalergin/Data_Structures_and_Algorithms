# Implementation of bubble sort algorithm

import random

def main():
    _list = random.sample(xrange(1, 101), 10)
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
