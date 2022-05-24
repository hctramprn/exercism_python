import re

def run():
    string = "Joe can't tell between 'large' and large."
    list_of_words = re.findall(r'[a-z0-9]+(?:\'[a-z]+)?', string.lower(), re.IGNORECASE)
    word_count = {word.strip("'"): list_of_words.count(word.strip("'")) for word in list_of_words}

    print(word_count)

if __name__ == '__main__':
    run()
