punctuation = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'


def count_words(sentence):
    string = ''
    for word in sentence.lower():
        for char in word:
            if char not in punctuation:
                if char != ' ':
                    string += char
                else:
                    string += ' '
            else:
                string += ' '

    list_of_words = [word.strip("'").strip('"') for word in string.split()]
    words_count = {word: list_of_words.count(word) for word in list_of_words}
    words_count.pop('', None)
    return words_count
