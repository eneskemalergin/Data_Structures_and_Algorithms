# Implementation of the Polynomial ADT using and array linked lists.

class Polynomial:
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)

        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.degree

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >=0, "Only non-empty polynomials can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    # Simple Brute Force method for polynomial addition
    def simple_add(self, rhsPoly):
        # REVIEW: Following line is not make sense
        newPoly = Polynomial()
        if self.degree() > rhsPoly.degree():
            maxDegree = self.degree()
        else:
            maxDegree = rhsPoly.degree()

        i = maxDegree
        while i >= 0:
            value = self[i] +rhsPoly[i]
            self.__appendTerm[i, value]
            i += 1
        # REVIEW: Ok, we are using it here but how we are changing it?
        return newPoly

    # Polynomial addition: newPoly = self + rhsPoly
    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0,
                "Addition only allowed on non-empty polynomials."

        newPoly = Polynomial()
        nodeA = self._termList
        nodeB = rhsPoly._termList

        # Add corresponding terms until one list is empty.
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            # elif listA.degree < listB.degree: Attention: This is a typo in the book
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            self._appendTerm(degree, value)

        # If self list contains more terms append them.
        while nodeA is not None:
            self._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        # or if rhs contains more terms append them.
        while nodeB is not None:
            self._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    # Polynomial substraction: newPoly = self - rhsPoly
    def __sub__(self, rhsPoly):
        pass

    # Polynomial multiplication: newPoly = self * rhsPoly
    def __mul__(self, rhsPoly):
        pass

    def multiply(self, rhsPoly):
        assert self.degree() >= and rhsPoly.degree() >= 0,
                "Multiplication only allowed on non-empty polynomials."

        # Create a new polynomial by multiplying rhsPoly by the first term.
        node = self._polyHead
        newPoly = rhsPoly._termMultiply(node)

        # Iterate through the remaining terms of the poly computing
        #  product of the rhsPoly by each term.
        node = node.next
        while node is not None:
            tempPoly = rhsPoly._termMultiply(node)
            newPoly = newPoly.add(tempPoly)
            node = node.next

        return newPoly

    # Helper method for creating a new polynomial from multiplying an
    #  existing polynomial by another term.
    def _termMultiply(self, termNode):
        newPoly = Polynomial()

        # Iterate through the terms and compute the product of each term and
        #  the term in termNode

        curr = curr.next
        while curr is not None:
            # Compute the product of the term.
            newDegree = curr.degree + termNode.degree
            newCoeff = curr.coefficient * termNode.coefficient

            # Append it to the new polynomial.
            newPoly._appendTerm(newDegree, newCoeff)

            # Advance the current pointer.
            curr = curr.next

        return newPoly

    # Helper method for appending terms to the polynomial
    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm

            self._polyTail = newTerm

# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
