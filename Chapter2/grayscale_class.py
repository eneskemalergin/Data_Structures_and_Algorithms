# Implementation of GrayscaleImage ADT
from array_class import Array2D

class GrayscaleImage:
    """
    GrayscaleImage(nrows, ncols) -> Constructor
    width() -> return width
    height() -> return height
    clear() -> clears entire image
    getitem() -> returns the intensity level of given pixel
    setitem() -> Sets the intensity level of the given pixel


    """
    # Creates a new instance that consists of nrows and ncols of pixels
    # each set to an initial value of 0.
    def __init__(self, nrows, nrols):
        self._theImage = Array2D(nrows, ncols)
        self._theImage.clear(0)
        # Initial value of 0 how?

    # Returns the width of the image.
    def width(self):
        return self._theImage.numCols()

    # Returns the height of the image.
    def height(self):
        return self._theImage.numRows()

    # Clears the entire image by setting each pixel to the given intensity value
    # The intensity value must be between [0:255]
    # Check This...
    def clear(self, value):
        return self._theImage.clear(value)

    # Returns the intensity level of the given pixel.
    # The pixel coordinates must be within the range.
    def __getitem__(self, row, col):
        assert row >= 0 and row < self.height() \
                and col >= 0 and col < self.width(), \
                "Array subscript out of range."
        return self._theImage[row, col]

    # Set's the intensity level of the given pixel to the given value.
    # The pixel coordinates must be within the valid range.
    # The intensity value must be between [0:255]
    def __setitem__(self, row, col, value):
        assert value >= 0 or  value <= 255, "Intensity level out of range."
        assert row >= 0 and row < self.height() \
                and col >= 0 and col < self.width(), \
                "Array subscript out of range."
        self._theImage[row, col] = value
