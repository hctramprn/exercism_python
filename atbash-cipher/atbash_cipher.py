import re

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encode(plain_text):
    """Function that returns a string encoded by the Atbash Cipher system.

    :param plain_text: str - Text that will be transposed.
    :return: str - Ciphered text.

    This function encodes a given text by the Atbash Cipher system.
    """

    table = plain_text.maketrans(ALPHABET + ALPHABET.upper(), ALPHABET[::-1]*2)
    text_encode = (plain_text.translate(table))
    str = ''.join(re.findall(r'[a-z0-9]', text_encode))
    str_enconde = ' '.join([str[i:i + 5] for i in range(0, len(str), 5)])
    return str_enconde


def decode(ciphered_text):
    """Function that returns a string decoded by the Atbash Cipher system.

    :param plain_text: str - Text that will be transposed.
    :return: str - Decoded text.

    This function decodes a given text by the Atbash Cipher system.
    """
    parsed_text = ''.join(ciphered_text.split())
    table = parsed_text.maketrans(ALPHABET[::-1], ALPHABET)
    text_decode = parsed_text.translate(table)
    return text_decode
