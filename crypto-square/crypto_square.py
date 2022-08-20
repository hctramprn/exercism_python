import re
import math


def cipher_text(plain_text):
    """Function that ciphers a given text into a square form.

    :param plan_text: str - Text to cypher.
    :return: str - Cyphered text in square format.

    This function cyphers a given text excluding spaces and special characters.
    """
    
    # returns an empty string in case no text is passed
    if plain_text == '':
        return ''
    
    # regular expression that finds and normalize the characters that match the criteria
    match_str = ''.join(re.findall(r'\w', plain_text)).lower()

    # defines the chunks that will be cyphered
    len_string = len(match_str)
    columns = math.ceil(len_string**(0.5))
    chunks = [match_str[i:i + columns] for i in range(0, len_string, columns)]

    # transpose the chunks
    square_txt = []
    for i in range(columns):
        x = ''
        for chk in chunks:
            # if the chunk is out of index, assigns a space
            try:
                x += chk[i]
            except:
                x += ' '
                continue
        square_txt.append(x)
    # returns the text
    return ' '.join(square_txt)
