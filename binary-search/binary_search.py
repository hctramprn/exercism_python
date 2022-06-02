def find(search_list, value):
    start = 0
    end = len(search_list) -1

    while start <= end:
        mid = start + (end - start) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    raise ValueError("value not in array")