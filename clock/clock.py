from datetime import time, timedelta


class Clock:
    def __init__(self, hour, minute):
        self.time_seconds = int(
            timedelta(0, 0, 0, 0, minute, hour).total_seconds())
        self.hours = (self.time_seconds // 3600) % 24
        self.minutes = (self.time_seconds // 60) % 60
        self.time = time(self.hours, self.minutes)

    def __repr__(self):
        # unambiguous representation of the clock object
        return f'Clock({self.time.hour}, {self.time.minute})'

    def __str__(self):
        # human friendly representation of the clock object
        return f'{self.time.strftime("%H:%M")}'

    def __eq__(self, other):
        # clock comparations
        t1 = self.time
        t2 = other
        return t1 == t2

    def __add__(self, minutes):
        t1 = self.time
        # delta time of the addition of the clock time and the minutes passed
        t_delta = timedelta(0, 0, 0, 0, t1.minute, t1.hour) + \
            timedelta(0, 0, 0, 0, minutes)
        # get the number of hours and minutes from the amount of seconds in the delta
        td_hours = int((t_delta.total_seconds() // 3600) % 24)
        td_minutes = int((t_delta.total_seconds() // 60) % 60)
        # creates a new object time with the given hours and minutes
        time_addition = time(td_hours, td_minutes)
        # returns the time in HH:MM format
        return f'{time_addition.strftime("%H:%M")}'

    def __sub__(self, minutes):
        t1 = self.time
        # delta time of the addition of the clock time and the minutes passed
        t_delta = timedelta(0, 0, 0, 0, t1.minute, t1.hour) - \
            timedelta(0, 0, 0, 0, minutes)
        # get the number of hours and minutes from the amount of seconds in the delta
        td_hours = int((t_delta.total_seconds() // 3600) % 24)
        td_minutes = int((t_delta.total_seconds() // 60) % 60)
        # creates a new object time with the given hours and minutes
        time_addition = time(td_hours, td_minutes)
        # returns the time in HH:MM format
        return f'{time_addition.strftime("%H:%M")}'
