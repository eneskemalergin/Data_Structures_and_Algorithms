from __future__ import division
from math import sqrt

class Point:
    # Constructs the point object with x and y values
    def __init__( self, x, y ):
        self._xcoord = x
        self._ycoord = y

    # Returns the x coordinate
    def getX( self ):
        return self._xcoord

    # Returns the y coordinate
    def getY( self ):
        return self._ycoord

    # shifts x and y coordinates with given values xInc, yInc
    def shift( self, xInc, yInc ):
        self._xcoord += xInc
        self._ycoord += yInc

    # Calculates and returns the distance between x,y point to given pointB
    def distance( self, pointB ):
        xDiff = self._xcoord - pointB._xcoord
        yDiff = self._ycoord - pointB._ycoord
        return sqrt( xDiff ** 2 + yDiff ** 2 )
