"""

Sort Dates
Datetimes are infamously a pain in the neck for programming. The least of the list of problems are the order of the year, month and day of a calendar date. Some countries use day-month-year format, others use year-month-day. Some insane countries use month-day-year because they want everyone else to be miserable.

Assignment
Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format and returns a list of the dates sorted in ascending order.

"""

from datetime import datetime

def sort_dates(dates):
    dates_tupel = [(date.split("-")[2], date.split("-")[0], date.split("-")[1]) for date in dates]
    new_dates = [datetime(int(date[0]), int(date[1]), int(date[2])) for date in dates_tupel]
    new_dates.sort()
    return [date.strftime("%m-%d-%Y") for date in new_dates]
