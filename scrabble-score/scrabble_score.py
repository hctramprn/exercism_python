scores = {1: ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R',
              'S', 'T'), 2: ('D', 'G'), 3: ('B', 'C', 'M', 'P'), 4: ('F', 'H', 'V', 'W', 'Y'), 5: ('K'), 8: ('J', 'X'), 10: ('Q', 'Z')}


def score(word):
    score = 0
    for char in word.upper():
        for points in scores:
            if char in scores[points]:
                score += points
    return score
