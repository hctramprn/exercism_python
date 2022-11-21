from datetime import date
from calendar import monthrange

orders = {'first': 0, 'second': 1, 'third': 2,
          'fourth': 3, 'fifth': 4, 'last': -1}


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message
    


def meetup(year, month, week, day_of_week):
    # declares the list that will store the possible matches
    day_matches = []
    #defines the last day of the given month
    date_range = (1, monthrange(year, month)[1] + 1)

    # loop that gets all the days that match the given day_of_week
    for day in eval(f'range{date_range}'):
        d = date(year, month, day)
        if d.strftime('%A') == day_of_week:
            day_matches.append(day)

    # if the 'teenth' parameter is passed, gets the day that is in the range 13 - 19
    if week == 'teenth':
        teenth = list((set(range(13, 20))).intersection(day_matches))
        return date(year, month, teenth[0])
    # else, checks if the asked day exist. Else it raises an error
    else:
        try:
            matched_day = date(year, month, day_matches[orders[week]])
        except:
            raise MeetupDayException("That day does not exist.")
        return matched_day
