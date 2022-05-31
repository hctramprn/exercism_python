def is_valid(isbn):
    isbn_parsed = isbn.replace('-', '')

    if len(isbn_parsed) != 10:
        return False
    if 'X' in list(isbn_parsed) and 'X' != isbn_parsed[-1]:
        return False

    isbn_list = [num.replace('X', '10') for num in [digit for digit in isbn.replace(
        '-', '') if digit.isdecimal() or digit == 'X']]

    isbn_validation_list = [int(value)*(10 - i)
                            for i, value in enumerate(isbn_list)]

    if len(isbn_validation_list) == 10:
        return sum(isbn_validation_list) % 11 == 0
    return False
