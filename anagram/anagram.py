def find_anagrams(word, candidates):
    candidates = [wrd for wrd in candidates if wrd.lower() != word.lower()]
    word = sorted(word.lower())
    words = [candidate for candidate in candidates if word == sorted(candidate.lower())]
    return words
