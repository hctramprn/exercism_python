import re


def response(hey_bob):
    sentence = ''.join(re.findall(r'[a-zA-Z0-9?]+', hey_bob))

    if len(sentence):
        if sentence.isupper():
            if hey_bob[-1] == '?':
                return "Calm down, I know what I'm doing!"
            return "Whoa, chill out!"
        elif hey_bob.strip()[-1] == '?':
            return "Sure."
        else:
            return "Whatever."
    return "Fine. Be that way!"