# Counting occurrences in text file using Array ADT
from array_class import Array1D

# Array theCounters created with size of 127 (ASCII characters)
theCounters = Array1D(127)
# theCounters elements initialized to 0
theCounters.clear(0)

# Open the text file for reading and extract each line from the file
# and iterate over each character in the line.
theFile = open('textfile.txt', 'r')
for line in theFile:
    for letter in line:
        code = ord(letter)
        theCounters[code] += 1
# Close the file
theFile.close()

# Print the results. The uppercase letters have ASCII values in the range 65..90
# the lowercase letters are in the range 97..122.
for i in range(26):
    print("%c - %4d       %c - %4d" % (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]))
