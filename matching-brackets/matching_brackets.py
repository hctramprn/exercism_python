import re

def is_paired(input_string):
    """Function that returns if the a string of parentheses is correctly closed.

    :param input_string: str - String of parentheses.
    :return: bool - Returns True if the group of parentheses is correctly closed 

    This function returns True if the group of parentheses is correctly closed. Else it returns False.
    
    """
    input_string = ''.join(re.findall(r'[\(\)\{\}\[\]]', input_string))

    while re.search(r'\[\]|\(\)|\{\}', input_string):
        input_string = input_string.replace('()', '')
        input_string = input_string.replace('{}', '')
        input_string = input_string.replace('[]', '')
    
    return len(input_string) == 0
