# Implementation of the Sparse Matrix ADT using and array linked lists.
from array import Array

class SparseMatrix:
    # Create a sparse matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self.listOfRows = Array(numRows)

    # Return the number of rows in the matrix
    def numRows(self):
        return len(self._listOfRows)

    # Return the number of columns in the matrix
    def numRows(self):
        return self._numCols

    # Return the value of element (i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        # TODO: Complete the method
        pass

    # Set the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, value):
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next

        # See if the element is in the list
        if curNode is not None and curNode.col == col:
            # Remove the node
            if value == 0.0:
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    predNode.next = curNode.next
            else: # Change the node's value
                curNode.value = value

        # Otherwise, the element is not in the list.
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next == curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                predNode.next = newNode

    # Scale the matrix by the given scalar
    def scaleBy(self, scalar):
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.next

    # Create and return to a transpose of this matrix
    def transpose(self):
        # TODO: Complete the method
        pass

    # Matrix addition: newMatrix = self + rhsMatrix
    def __add__(self, rhsMatrix):
        # Making sure the two matrices have the correct size.
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes are not compatible for adding!"

       # Create a new sparse matrix of the same size.
       newMatrix = SparseMatrix(self.numRows(), self.numCols())

       # Add the elements of this matrix to the new matrix.
       for row in range(self.numRows()):
           curNode = self._listOfRows[row]
           while curNode is not None:
               newMatrix[row, curNode.col] = curNode.value
               curNode = curNode.next

       # Add the elements of the rhsMatrix to the new matrix.
       for row in range(rhsMatrix.numRows()):
           curNode = rhsMatrix._listOfRows[row]
           while curNode is not None:
               value = newMatrix[row, curNode.col]
               value += curNode.value
               newMatrix[row, curNode.col] = value
               curNode = curNode.next

       return newMatrix

   # TODO: 1- Add Matrix Substraction: __sub__
   # TODO: 2- Add Matrix Multiplication: __mul__

# Storage class for creating matrix element nodes.
class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None
