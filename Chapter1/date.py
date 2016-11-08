# Implements a proleptic Gregorian calendar date as a Julian day number

class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), "Invalid Gregorian date."

        # If first line of the equation, T = (M-14)/12, has to be changed
        # since Python's implemenation of integer division is not the same
        # as the mathematical definition.
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
                (1461 * (year + 4800 + tmp) // 4) + \
                (367 * (month - 2 - tmp * 12) // 12) - \
                (3 * ((year + 4900 + tmp) // 100) // 4)

    # Returns the date as a string in Gregorian format.
    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    # Returns the month as an integer
    def month(self):
        return (self._toGregorian())[0] # Returns M from (M, d, y)

    # Returns the day as an integer
    def day(self):
        return (self._toGregorian())[1] # Returns D from (m, D, y)

    # Returns the year as an integer
    def year(self):
        return (self._toGregorian())[2] # Returns Y from (m, d, Y)

    # Returns day of the week as and int between 0 (mon), and 6 (sun)
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    # Returns the month name from given date
    def monthName(self):
        """
        Returns the month's name
        1 -> January
        12 -> December
        """
        monthdict = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                     6:"June", 7:"July", 8:"August", 9:"September",
                     10:"October", 11:"November", 12:"December"}
        month = self._toGregorian()[0]
        return monthdict[month]

    # Checks the year if it's leap year or not
    def isLeapYear(self):
        """
        Leap Year follows:
        The year can be evenly divided by 4;
        If the year can be evenly divided by 100, it is NOT a leap year, unless;
        The year is also evenly divisible by 400. Then it is a leap year.
        """
        year = self._toGregorian()[3]
        leapyear = False
        if year % 4 == 0:
            leapyear = True
        if year % 100 == 0:
            leapyear = False
        if year % 400 == 0:
            leapyear = True
        return leapyear

    # Returns the number of days in given month
    def numDays(self):
        monthLenDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
                        10:31, 11:31, 12:30}
        month = self._toGregorian()[0]
        if month == 2 and self.isLeapYear():
            return 29
        else:
            return monthLenDict[month]

    # Advances the date by given number of days
    def advanceBy(self, numDays):
		self._julianDay += numDays

    # Returns the name day of week from given date.
    def dayOfWeekName(self):
		weekNames={0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday",
                   4:"Friday", 5:"Saturday", 6:"Sunday"}
		return weekNames[self.dayOfWeek()]

    # Returns the day of year from 0 to 365/366
    def dayOfYear(self):
		month,day,year = self._toGregorian()
		dayYear=0
		if self.isLeapYear(year):
			monthList = [0,31,29,31,30,31,30,31,31,30,31,30,31]
			for i in range(0,month):
				dayYear+=monthList[i]
			return dayYear + day
		else:
			monthList = [0,31,28,31,30,31,30,31,31,30,31,30,31]
			for i in range(0,month):
				dayYear+=monthList[i]
			return dayYear + day

            # Checks if the date is a weekday
    def isWeekDay(self):
		return (self.dayOfWeek()>=0 and self.dayOfWeek()<=4)

    # Checks if the date is a spring or autumn equinox
    def isEquinox( self ):
        return (self.day() == 20 and self.month() == 3) or \
               (self.day() == 22 and self.month() == 9)
   # Check if the date is the summer or winter solstice
    def isSolstice( self ):
        return (self.day() == 21 and self.month() == 6) or \
               (self.day() == 22 and self.month() == 12)

    # Logically compares the two dates.
	def comparable(self, otherDate):
		if self.__lt__(otherDate):
			return -1
		if self.__eq__(otherDate):
			return 0
		else:
			return 1

    # Checks if date is valid Gregorian or not
    def _isValidGregorian(self, month, day, year):
        if month < 1 or month > 12:
            return False
        if month == 1 or month == 3 or month == 5:
            if day < 1 or day > 31:
                return False
        elif month == 8 or month == 10 or month == 12:
            if day < 1 or day > 31:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                return False
        elif month == 2: #I explicitly do not account for leap years
            if day < 1 or day > 28:
                return False

    # string method with additional calendar divider    
    def asGreogrian( self, divchar = '/'):
        month, day, year = self._toGregorian()
        return '%02d%s%02d%s%04d' % (month, divchar, day, divchar, year)

    # Returns the Gregorian date as a tuple: (month, day, year)
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A //146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def printCalendar(self):
		month,day,year = self._toGregorian()
		self.advanceBy(-day+1)
		month,day,year = self._toGregorian()
		print self.dayOfWeekName()
		print (self.monthName()+" "+str(self.year())).center(50)
		print "Su  Mo  Tu  We  Th  Fr  Sa".center(50)
		result=""
		if self.isLeapYear(year):
			monthList = [0,31,29,31,30,31,30,31,31,30,31,30,31]
		else:
			monthList = [0,31,28,31,30,31,30,31,31,30,31,30,31]
		for i in range(1,monthList[month]+1):
			result+=str(i)
		print result.center(50)
