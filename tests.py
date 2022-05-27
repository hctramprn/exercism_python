import re

hey_bob = 'Okay if like my  spacebar  quite a bit?   '


def run():
    sentence = ''.join(re.findall(r'[a-zA-Z0-9?]+', hey_bob))

    if len(sentence):
        if sentence.isupper():
            if hey_bob[-1] == '?':
                print("Calm down, I know what I'm doing!")
            print("Whoa, chill out!")
        elif hey_bob.strip()[-1] == '?':
            print("Sure.")
        else:
            print("Whatever.")
    print("Fine. Be that way!")



if __name__ == '__main__':
    run()
