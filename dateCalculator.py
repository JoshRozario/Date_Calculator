import re
from date import Date, daysInMonth, isLeapYear


def dateCalc(date1: Date, date2: Date):
    days = date2 - date1
    if days < 0:
        days = 0
    return(days)


def isValidDate(date):
    datePattern = "[0-3][0-9]\/[0-1][0-9]\/[0-9]{4}"
    if(re.search(datePattern, date)):
        splitDate = date.split("/")
        if int(splitDate[1]) <= 12 and int(splitDate[0]) <= daysInMonth(splitDate[1], isLeapYear(splitDate[2])):
            return True
        else:
            return False
    else:
        return False


def dateFormatter():
    while True:
        date = input()
        if not isValidDate(date):
            print(
                "Invalid date or format, please enter a valid date in the format of DD/MM/YYYY: ", end='')
            continue
        else:
            splitDate = date.split("/")
            return Date(splitDate[0], splitDate[1], splitDate[2])


# Assumptions made:
# Date order doesn't matter
# Only DD/MM/YYYY formatted dates are allowed
def main():
    print("Welcome to the date calculator!")
    while True:
        print("Please enter the first date: ", end='')
        date1 = dateFormatter()
        print("Please Enter the second date: ", end='')
        date2 = dateFormatter()
        dates = sorted((date1, date2))
        days = dateCalc(dates[0], dates[1])
        print("there are", days, "days between the two dates")
        return days


if __name__ == '__main__':
    main()
