from itertools import permutations

ALLERGIES = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
             'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128}


def run():
    score = 257
    if score > 256:
        pwr = 0
        while score - (2**pwr) > 255:
            pwr += 1
        return score - (2**pwr)
    return score

    # lst = [16, 1, 8]
    # allergies = []
    # for comb in sorted(lst):
    #     for allergen, score in ALLERGIES.items():
    #         if comb == score:
    #             allergies.append(allergen)
    # print(allergies)


if __name__ == '__main__':
    run()
