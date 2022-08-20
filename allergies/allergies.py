from itertools import permutations

ALLERGIES = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
             'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128}


class Allergies:

    def __init__(self, score):
        self.score = self.score_adjust(score)
        self.combination = self.combinations()

    def score_adjust(self, score):
        score = score
        if score > 256:
            pwr = 8
            while score - (2**pwr) > 256:
                pwr += 1
            return score - (2**pwr)
        return score

    def combinations(self):
        perm = list(permutations([1, 2, 4, 8, 16, 32, 64, 128], 8))
        for combination in perm:
            n = 0
            for i in range(8):
                n += combination[i]
                if self.score - n == 0:
                    return combination[:i + 1]

    def allergic_to(self, item):
        if self.score == 0:
            return False
        return ALLERGIES[item] in self.combination

    @property
    def lst(self):
        lst = self.combination
        if lst != None:
            allergies = []
            for comb in lst:
                for allergen, score in ALLERGIES.items():
                    if comb == score:
                        allergies.append(allergen)
            return allergies
        return []
