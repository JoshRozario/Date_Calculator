class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, obj):
        return (self.year, self.month, self.day) < (obj.year, obj.month, obj.day)

    def __gt__(self, obj):
        return (self.year, self.month, self.day) > (obj.year, obj.month, obj.day)

    def __le__(self, obj):
        return (self.year, self.month, self.day) <= (obj.year, obj.month, obj.day)

    def __ge__(self, obj):
        return (self.year, self.month, self.day) >= (obj.year, obj.month, obj.day)

    def __eq__(self, obj):
        return (self.year, self.month, self.day) == (obj.year, obj.month, obj.day)

    def __sub__(self, other):
        result = Date((int(self.day)-1) - int(other.day), int(self.month) -
                      int(other.month), int(self.year)-int(other.year))
        leapYear = isLeapYear(self.year)
        year = daysBetweenYears(self.year, other.year)  # 365 * result.year
        month = daysBetweenMonths(self.month, other.month, leapYear)
        day = (int(self.day)-1) - int(other.day)
        # print(year, month, day, leapYearDayChecker(self, other))
        return year + month + day + leapYearDayChecker(self, other)

    def __str__(self):
        return self.day + '/' + self.month + '/' + self.year

    def __repr__(self):
        return str((self.day, self.month, self.year))


def daysBetweenMonths(month1, month2, leapYear):
    days = 0
    # if months in same year
    if month1 >= month2:
        beggining = int(month2)
        ending = int(month1)
        for month in range(beggining, ending):
            days += daysInMonth(month, leapYear)

    # if going into next year
    else:
        beggining = int(month1)
        ending = int(month2)
        for month in range(beggining, ending):
            days -= daysInMonth(month, leapYear)
    return days


def daysBetweenYears(endingYear, beginningYear):
    days = 0
    for year in range(int(beginningYear), int(endingYear)):
        days += 365 + isLeapYear(year)
    return days


def isLeapYear(year):
    year = int(year)
    if (year % 4 == 0):
        if (year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(month, leapyear):
    month = int(month)
    if (month == 2):
        return 28+leapyear
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    else:
        return 30


def leapYearDayChecker(self: Date, other: Date):
    if int(self.month) > 2 and int(other.month) > 2 and isLeapYear(self.year) and other.year != self.year:
        return 1
    elif int(self.month) > 2 and int(other.month) > 2 and not isLeapYear(self.year) and other.year != self.year:
        return -1

    else:
        return 0
