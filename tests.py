punctuation = '!#$%&()*+,-./:;<=>?@[\]^_`{|}~'
original = ["word", "one of each", "one fish two fish red fish blue fish", "one,two,three", "one,\ntwo,\nthree", "car: carpet as java: javascript!!&@$%^&", "testing, 1, 2 testing", "go Go GO Stop stop", "'First: don't laugh. Then: don't cry. You're getting it.'",
            "Joe can't tell between 'large' and large.", "Joe can't tell between app, apple and a.", " multiple   whitespaces", ",\n,one,\n ,two \n 'three'", "rah rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance", "hey,my_spacebar_is_broken", "''hey''"]


def run():
    for sentence in original:
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
        print(words_count)


        #print(string)








    # sentence = original.lower()
    # ascii_sentence = ''
    # for char in sentence.lower():
    #     if char not in punctuation:
    #         ascii_sentence += char
    #     else:
    #         ascii_sentence += ' '
    # print(ascii_sentence)
    # ascii_sentence = ascii_sentence.strip().split()
    # if "'" in ascii_sentence:
    #     ascii_sentence.remove("'")
    # words_count = {word: ascii_sentence.count(word) for word in ascii_sentence}
    # print(words_count)
if __name__ == '__main__':
    run()
