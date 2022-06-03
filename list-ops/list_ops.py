def append(list1, list2):
    return list1 + list2


def concat(lists):
    concat_list = []
    for element in lists:
        concat_list += element
    return concat_list


def filter(function, list):
    fun = function
    filtered_list = []
    for element in list:
        if fun(element):
            filtered_list += [element]
    return filtered_list


def length(list):
    len = 0
    for element in list:
        len += 1
    return len


def map(function, list):
    fun = function
    map_list = []
    for element in list:
        map_list += [fun(element)]
    return map_list


def foldl(function, list, initial):
    value = initial
    for element in list:
        value = function(value, element)
    return value


def foldr(function, list, initial):
    value = initial
    for element in list[::-1]:
        value = function(element, value)
    return value


def reverse(list):
    return list[::-1]
