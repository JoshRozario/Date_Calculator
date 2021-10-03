import unittest
import dateCalculator
import calendar

from dateCalculator import Date, dateFormatter, dateCalc


class TestIsDateCalc(unittest.TestCase):

    def setUp(self):
        self.givenDates1 = sorted((
            Date("02", "06", "1983"), Date("22", "06", "1983")))
        self.givenDates2 = sorted((
            Date("04", "07", "1984"), Date("25", "12", "1984")))
        self.givenDates3 = sorted((
            Date("03", "01", "1989"), Date("03", "08", "1983")))
        self.givenDates4 = sorted((
            Date("01", "01", "2000"), Date("03", "01", "2000")))

        self.onedaydifference = sorted((
            Date("03", "01", "1984"), Date("04", "01", "1984")))

        self.sameDay = sorted((
            Date("03", "01", "1984"), Date("04", "01", "1984")))

        self.goingIntoLeapYear = sorted((
            Date("03", "08", "1999"), Date("03", "08", "2000")))

        self.fromLeapYear = sorted((
            Date("03", "08", "2000"), Date("03", "08", "2001")))

        self.leapYearinFebMultipleYears = sorted(
            (Date("23", "02", "2007"), Date("29", "02", "2344")))

        self.normalYearinFebMultipleYears = sorted(
            (Date("23", "02", "2007"), Date("28", "02", "2343")))

        self.normalYearMultipleYears = sorted(
            (Date("23", "02", "2007"), Date("28", "03", "2343")))

        self.givenDates1Reversed = sorted((
            Date("22", "06", "1983"), Date("02", "06", "1983")))
        self.givenDates2Reversed = sorted((
            Date("25", "12", "1984"), Date("04", "07", "1984")))
        self.givenDates3Reversed = sorted((
            Date("03", "08", "1983"), Date("03", "01", "1989")))
        self.givenDates4Reversed = sorted((
            Date("03", "01", "2000"), Date("01", "01", "2000")))

    def tearDown(self):
        pass

    def LeapYear(self, year):
        result = dateCalculator.isLeapYear(year)
        self.assertEqual(result, calendar.isleap(
            year), 'failed with year:' + str(year))

    def test_leapYear(self):
        for years in range(1901, 3000):
            self.LeapYear(years)

    # correct dates were checked using https://www.timeanddate.com - 1
    def test_givenExamples(self):
        self.assertEqual(
            dateCalc(self.givenDates1[0], self.givenDates1[1]), 19)

        self.assertEqual(
            dateCalc(self.givenDates2[0], self.givenDates2[1]), 173)

        self.assertEqual(
            dateCalc(self.givenDates3[0], self.givenDates3[1]), 1979)

        self.assertEqual(
            dateCalc(self.givenDates4[0], self.givenDates4[1]), 1)

    def test_edgeCases(self):
        self.assertEqual(
            dateCalc(self.onedaydifference[0], self.onedaydifference[1]), 0)

        self.assertEqual(
            dateCalc(self.sameDay[0], self.sameDay[1]), 0)

        self.assertEqual(
            dateCalc(self.goingIntoLeapYear[0], self.goingIntoLeapYear[1]), 365)

        self.assertEqual(
            dateCalc(self.fromLeapYear[0], self.fromLeapYear[1]), 364)

        self.assertEqual(
            dateCalc(self.leapYearinFebMultipleYears[0], self.leapYearinFebMultipleYears[1]), 123091)

        self.assertEqual(
            dateCalc(self.normalYearinFebMultipleYears[0], self.normalYearinFebMultipleYears[1]), 122725)

        self.assertEqual(
            dateCalc(self.normalYearMultipleYears[0], self.normalYearMultipleYears[1]), 122753)

    # This is basically just run to confirm that the Sorted function works fine with the class
    def test_reverseOrder(self):

        self.assertEqual(
            dateCalc(self.givenDates1Reversed[0], self.givenDates1Reversed[1]), 19)

        self.assertEqual(
            dateCalc(self.givenDates2Reversed[0], self.givenDates2Reversed[1]), 173)

        self.assertEqual(
            dateCalc(self.givenDates3Reversed[0], self.givenDates3Reversed[1]), 1979)

        self.assertEqual(
            dateCalc(self.givenDates4Reversed[0], self.givenDates4Reversed[1]), 1)


if __name__ == '__main__':
    unittest.main()
