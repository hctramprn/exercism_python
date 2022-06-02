ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def rotate(text, key):
    """Function that returns a cipher of a given string.

    :param text: str - String that should transposed.
    :param key: int - Number of positions that the cipher will take.
    :return: str - The original text string transposed.

    This function returns a string after it is transposed by a given cipher.

    """
    table = ALPHABET[key:] + ALPHABET[:key]
    mk_trans = str.maketrans(ALPHABET + ALPHABET.upper(), table + table.upper())
    return text.translate(mk_trans)
