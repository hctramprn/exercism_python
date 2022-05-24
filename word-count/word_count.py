import re


def count_words(sentence):
    list_of_words = re.findall(r'[a-z0-9]+(?:\'[a-z]+)?', sentence.lower(), re.IGNORECASE)
    word_count = {word: list_of_words.count(word) for word in list_of_words}
    return word_count
