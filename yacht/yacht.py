# Score categories.
# Change the values as you see fit.
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: 1 * x.count(1)
TWOS = lambda x: 2 * x.count(2)
THREES = lambda x: 3 * x.count(3)
FOURS = lambda x: 4 * x.count(4)
FIVES = lambda x: 5 * x.count(5)
SIXES = lambda x: 6 * x.count(6)
FULL_HOUSE = lambda x: sum(x) if set(x.count(y) for y in x) == {2, 3} else 0
FOUR_OF_A_KIND = lambda x: sum(set(y for y in x if x.count(y) >= 4)) * 4
LITTLE_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and min(x) == 1 and max(x) == 5 else 0
BIG_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and min(x) == 2 and max(x) == 6 else 0
CHOICE = lambda x: sum(x)


def score(dice, category):
    return category(dice)
