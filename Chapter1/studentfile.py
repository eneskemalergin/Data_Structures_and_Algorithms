# Implementation of the StudentFileReader ADT using a text file as the
# input source in which each field is stored on a separate line.

class StudentFileReader:
    # Create a new student reader instance.
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputSrc = None

    # Open a connection to the input file.
    def open(self):
        self._inputFile = open(self._inputSrc, "r")

    # Close the connection to the input file.
    def close(self):
        self._inputFile.close()
        self._inputFile = None

    # Extract all student record and store them in a list.
    def fetchAll(self):
        theRecords = list()
        student = self.fethcRecord()
        while student != None:
            theRecords.append(student)
            student = self.fethcRecord()
        return theRecords

    # Extract the next student record from the file.
    def fetchRecord(self):
        # Read the first line of the record.
        line = self._inputFile.readline()
        if line == "":
            return None

        # If there is another record, create a storage object and fill it.
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student




# Storage class used for an  individual student record.
class StudentRecord():
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
