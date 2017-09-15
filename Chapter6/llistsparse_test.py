# Testing script for linked list implementation of Sparse Matrix ADT

from llistsparse import SparseMatrix

def main():
    print("Testing class constructor:")
    LLSMatrix = SparseMatrix(3,3) # Creating a zero sparse matrix 3x3

    print("Testing numRows method:")
    print(LLSMatrix.numRows())

    print("Testing numCols method:")
    print(LLSMatrix.numCols())

    print("Testing getitem method:")
    # This method is not complete
    # print(LLSMatrix[1,2])

    print("Testing setitem method:")
    # If error not occured everything works.
    LLSMatrix[1,2] = 1 # Setting item to the given index location

    print("Testing scaleBy method: ")
    LLSMatrix.scaleBy(2)

    print("Testing transpose method: ")
    # This method is not complete
    # LLSMatrix.transpose()

    print("Testing add method: ")
    # To test this second sparse matrix is needed
    LLSMatrix2 = SparseMatrix(4,5)
    LLSMatrix3 = SparseMatrix(3,2)
    temp = LLSMatrix + LLSMatrix3 # This should be able to work
    new_temp = LLSMatrix + LLSMatrix2

    print("Testing substraction method: ")
    # This method is not complete
    # temp = LLSMatrix - LLSMatrix3 # This should be able to work
    # new_temp = LLSMatrix - LLSMatrix2 # This should give error

    

if __name__ == '__main__':
    main()
