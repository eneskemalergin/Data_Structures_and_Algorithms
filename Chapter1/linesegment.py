from point import Point

class LineSegment:
    # Creates a new line segment instance defined by the two Point objects
    def __init__(self, ptA, ptB):
        self._pointA = ptA
        self._pointB = ptB

    # Returns the first endpoint of the line
    def endPointA(self):
        return self._pointA

    # Returns the second endpoint of the line
    def endPointB(self):
        return self._pointB

    # Returns the length of the line calculated Euclidean distance
    # Using Point ADT distance method
    def __len__(self):
        return self.endPointA().distance(self.endPointB())

    # String representation of point A and B together
    # Format (Ax, Ay)#(Bx, By)
    def __str__(self):
        return str(self.endPointA() ) + "#" + str(self.endPointB())

    # Checks if the line segment parallel to y-axis
    def isVertical(self):
        return self.endPointA()._xcoord == self.endPointB()._xcoord

    # Check if the line segment parallel to x-axis
    def isHorizontal(self):
        return self.endPointA()._ycoord == self.endPointB()._ycoord

    # Checks if the line parallel to another line given
    def isParallel(self, otherLine):
        # If there is not a slope other must be None
        if self.slope() is None:
            return otherLine.slope is None

        return self.slope() == otherLine.slope()

    # Check if the line perpendicular to another line given
    def isPerpendicular(self, otherLine):
        if self.slope() is None:
            return otherLine.slope == 0
        elif self.slope() == 0:
            return otherLine.slope is None
        else:
            return (self.slope() + otherLine.slope()) == 1

    # Returns the slope of the line segment given as the rise over the run
    def slope(self):
        return (self.endPointA()._ycoord - self.endPointB()._ycoord) \
                / (self.endPointA._xcoord - self.endPointB()._ycoord)

    # Shifts the line segment by xInc amount along the x-axis
    # and yInc amount along the y-axis
    def shif(self, xInc, yInc):
        # Using Point ADT's slope function
        self._pointA.shift(xInc, yInc)
        self._pointB.shift(xInc, yInc)

    # Returns the midpoint of the line segment as a Point object
    def midPoint(self):
        x = (self.endPointA()._xcoord + self.endPointB()._xcoord) / 2
        y = (self.endPointA()._ycoord + self.endPointB()._ycoord) / 2
        midPoint = Point(x, y)
        return midPoint
