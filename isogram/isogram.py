def is_isogram(string):
    string = string.lower().replace(' ', '-').replace('-', '')
    return len(list(string)) == len(set(string))
