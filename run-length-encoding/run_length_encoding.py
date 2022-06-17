import re
import string as st


def decode(string):
    """Function that returns a decoded string by the Run-Length method.

    :param string: str - Encoded string.
    :return: str - Decoded string.
    
    This function recieves a string as parameter and decodes it using the Run-Length method.
    """
    # Creates the list of letter groups in the encoded string
    lst = re.findall(r'\d*\D', string, re.IGNORECASE)

    # Splits the frecuency and the letters into subgroups
    char_lst = [re.findall(r'[0-9]+|[a-zA-Z ]', group) for group in lst]
    
    # Creates the decoded string
    decoded = ''
    for chars in char_lst:
        if len(chars) > 1:
            decoded += chars[1] * int(chars[0])
        else:
            decoded += chars[0]
    return decoded


def encode(string):
    """Function that returns an encoded string by the Run-Length method.

    :param string: str - Decoded string.
    :return: str - Encoded string.
    
    This function recieves a string as parameter and encodes it using the Run-Length method.
    """
    # Splits the alphabet into different OR groups for the regex pattern
    regx = '+|'.join(st.ascii_letters) + '+| +'

    # Creates the list of groups in the string
    lst = re.findall(regx, string)

    # Creates de encoded string
    encoded = ''
    for el in lst:
        encoded += f'{len(el) if len(el) > 1 else ""}{el[0]}'
    return encoded
