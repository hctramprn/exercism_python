def find(search_list, value):
    """Function that returns the index of a given value in a sorted array.

    :param search_list: list - Array in which the function will search for the value.
    :param value: int - Value that the function will search in the array.
    :return: int - Index of the given value in the array.

    This function returns the index of a given value inside an array. In case the value is not in the array, the function raises a ValueError.

    """

    start = 0
    end = len(search_list) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    raise ValueError("value not in array")
