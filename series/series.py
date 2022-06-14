import re


def slices(series, length):
    """Function that returns all the contiguous substrings of n lenght.

    :param series: str - Series of numbers.
    :param length: int - Length of the substrings.
    :return: list - List of all the substrings that match de given length in the series.

    This function returns the substrings of n length in a given series. It will raise a ValueError in case the parameters could cause a conflict.

    """
    # Possible errors
    if not length:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not len(series):
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    # Regular expression that recieves the length of the substring
    regx = r'(?=(\d{' + str(length) + r'}))'
    lst = re.findall(regx, series)
    # List with all the matches
    return lst
