from itertools import combinations_with_replacement as comb


def find_fewest_coins(coins, target):
    # raises a ValueError if a negative target is passed
    if target < 0:
        raise ValueError("target can't be negative")
    # returns an empty list if zero is the target
    if target == 0:
        return []

    # reverses the list so that the biggest values
    # are the first to be processed
    c = sorted(coins, reverse=True)

    # inits the list that will hold the combinations
    candidate = []
    # while there's no combination, tries 20 times to find
    # a combination one num larger each time
    i = 1
    while not candidate and i < 20:
        combinations = [pair for pair in comb(c, i) if sum(pair) == target]
        if not combinations:
            i += 1
        else:
            candidate = combinations[0]

    # if the list is still empty, raises a ValueError
    if not candidate:
        raise ValueError("can't make target with given coins")

    # returns the list sorted from smallest to largest
    return sorted(candidate)
