import re


def abbreviate(words):
    return ''.join([word[0].upper() for word in re.findall(r'[a-z]+\'?[a-z]*', words, re.IGNORECASE)])
