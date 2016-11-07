# Modified version of checkdates.py
# Now we can store dates from user in our bag

from linearbag import Bag
from date import Date

def main():
    bornBefore = Date(6, 1, 1995)
    bag = Bag()

    # Extract dates from the user and place them in the bag.
    date = promptAndExtractDate()
    while date is not None:
        bag.add(date)
        date = promptAndExtractDate()

    # Iterate over the bag and check the age.
    for date in bag:
        if date <= bornBefore:
            print("Is at least 21 years of age: " + str(date))



# Prompts for and extracts the Gregorian date components. Returns a
# Date object or None when the user has finished entering dates.
def promptAndExtractDate():
    print( "Enter a birth date." )
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return Date(month, day, year)

if __name__ == '__main__':
    main()
