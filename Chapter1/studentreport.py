# Produces a student report from data extracted from and external source.
from studentfile import StudentFileReader

# Name of the file to open.
FILE_NAME = "students.txt"

def main():
    # Extract the students records from the given text file.
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    studentList = reader.fetchAll()
    reader.close()

    # Sort the list by id number. Each object is passed to the lambda
    # expression which returns the idNum field of the object.
    studentList.sort(key = lambda rec: rec.idNum)

    # Print the student report.
    printReport(studentList)

# Prints the student report.
def printReport(theList):
    # The class names associated with the class codes.
    classNames = (None, "Freshman", "Sophomore", "Junior", "Senior")

    # print the header.
    print("LIST OF STUDENTS".center(50))
    print("")
    print("%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))
    print("%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
    # Print the body
    for record in theList:
        print("%5d %-25s %-10s %4.2f" % (record.idNum, \
                                        record.lastName + ", " + record.firstName,
                                        classNames[record.classCode], record.gpa ))

    # Add a footer.
    print("-"*50)
    print("Number of Students: ", len(theList))


if __name__ == '__main__':
    main()
