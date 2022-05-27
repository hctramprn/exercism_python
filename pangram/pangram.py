import re
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(sentence):
    string = ''.join(re.findall(r'[a-zA-Z]+', sentence.lower()))
    for letter in alphabet:
        if letter not in string:
            return False
    return True

