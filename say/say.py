import re

order_dict = {1: '', 2: 'thousand', 3: 'million', 4: 'billion', 5: 'trillion'}

numbers_names = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}


def say(number):
    """Function that returns the name of a given number.

    :param number: int - Number.
    :return: str - Name of the given number.

    This function returns the name of a given number in the range from 0 to 999,999,999,999. If the given number is out of range, the function raises ValueErrors.

    """
    if number < 0:
        raise ValueError("input out of range")
    if number > 999999999999:
        raise ValueError("input out of range")
    if not number:
        return 'zero'

    chunks_lst = [chunk[::-1]
                  for chunk in re.findall(r'\d{1,3}', str(number)[::-1])][::-1]
    order = len(chunks_lst)
    number_name = ''

    for chunk in chunks_lst:
        chunk = str(int(chunk))
        # Checks if the chunk has hundreds
        if len(chunk) > 2:
            number_name += f'{numbers_names[int(chunk[0])]} hundred '

        # Checks if the last two digits are in the number_names dict
        if int(chunk[-2:]) in numbers_names:
            number_name += f' {numbers_names[int(chunk[-2:])]}'

        # Checks if the last two digits are different from zero and adds the tens
        elif int(chunk[-2:]) != 0:
            number_name += f'{tens[int(chunk[-2])]}'

            # Adds the last number in case it is different from zero
            if int(chunk[-1]) != 0:
                number_name += f'-{numbers_names[int(chunk[-1])]}'

        # Adds the order in each of the chunks
        if int(chunk):
            number_name += f' {order_dict[order]} '
        order -= 1
    return number_name.strip().replace('  ', ' ')
