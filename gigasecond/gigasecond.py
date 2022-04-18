
from datetime import timedelta


GIGASECOND = timedelta(seconds=10**9)


def add(moment):
    """Returns a moment after a gigasecond has passed.

    This function returns the moment after a gigasecond has passed.
    """
    return moment + GIGASECOND
