

def run():
    candidates = ["Eons", "ONES"]
    word = "nose"
    candidates = [wrd for wrd in candidates if wrd.lower() != word.lower()]
    word = sorted(word.lower())
    words = []
    for candidate in candidates:
        if word == sorted(candidate.lower()):
            words.append(candidate)
    print(words)





if __name__ == '__main__':
    run()
