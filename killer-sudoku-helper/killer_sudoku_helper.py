from itertools import permutations


def combinations(target, size, exclude):
    # converts the exclusion list into a set for future comparation
    exc = set(tuple(exclude))
    # creates all the possible combinations with the given parameters
    combinations = permutations(range(1, 10), size)
    # get all the combinations of numbers that sum the given target
    # it sorts them and convert the list into a set to remove duplicates
    candidates = list(set([tuple(sorted(can))
                      for can in combinations if sum(can) == target]))
    # converts each group of numbers into set to check membership
    candidates_set = [set(group) for group in candidates]
    # choose the groups that don't have any of the exluded numbers
    winners = sorted([sorted(list(w)) for w in candidates_set if w.isdisjoint(exc)])
    # returns the list of possible combinations
    return winners
