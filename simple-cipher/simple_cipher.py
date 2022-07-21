import random
import string


class Cipher:
    def __init__(self, key=None):
        # calls the function get_key and sets its value as an atribute
        self.key = self.get_key(key)
        # sets the deltas in each set of characters
        self.delta_key = [ord(char) - 97 for char in self.key]

    # sets a random 100 lowercase character string as a key if none is passed
    def get_key(self, key):
        if key is None:
            return ''.join(random.choices(string.ascii_lowercase, k=100))
        # else it returns the passed key
        return key

    def encode(self, text):
        # sets the lenght of the delta key to fullfill scenarios where the key is shorter than the message
        delta = self.delta_key * int((len(text) / len(self.delta_key)) + 1)
        # sets an empty array to store the encoded message
        encoded = []
        # loops through the message encoding the message
        for i in range(len(text)):
            x = ord(text[i])
            y = delta[i]
            # if char code is out of range, substracts 26 positions
            if x + y > 122:
                encoded.append(chr(x + y - 26))
            else:
                encoded.append(chr(x + y))
        # returns the joined array
        return ''.join(encoded)

    def decode(self, text):
        # sets the lenght of the delta key to fullfill scenarios where the key is shorter than the message
        delta = self.delta_key * int((len(text) / len(self.delta_key)) + 1)
        # sets an empty array to store the decoded message
        decoded = []
        # loops through the message encoding the message
        for i in range(len(text)):
            x = ord(text[i])
            y = delta[i]
            # if char code is out of range, adds 26 positions
            if x - y < 97:
                decoded.append(chr(x - y + 26))
            else:
                decoded.append(chr(x - y))
        # returns the joined array
        return ''.join(decoded)
