from collections import Counter
card_nums = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8


def check_straight(nums):
    if len(set(nums)) == 5 and nums[-1]-nums[0] == 4:
        return nums[-1]
    elif set(nums) == {10, 11, 12, 13, 1}:
        return 14
    return None


def check_hand(hand):
    cards = hand.split()
    nums = []
    suit_set = set()
    for c in cards:
        n, s = c[:-1], c[-1]
        suit_set.add(s)
        nums.append(card_nums.get(n) if n in card_nums else int(n))
    nums.sort()
    is_straight = check_straight(nums)
    nums = sorted([14 if n == 1 else n for n in nums])
    nums_counter = Counter(nums)
    if is_straight is not None and len(suit_set) == 1:
        return (STRAIGHT_FLUSH, is_straight)
    if len(set(nums)) == 2:
        n1, n2 = nums_counter.keys()
        if nums_counter[n1] < nums_counter[n2]:
            n1, n2 = n2, n1
        if max(nums_counter.values()) == 4:
            return (FOUR_OF_A_KIND, (n1, n2))
        else:
            return (FULL_HOUSE, (n1, n2))
    if len(suit_set) == 1:
        return (FLUSH, tuple(nums[::-1]))
    if is_straight is not None:
        return (STRAIGHT, is_straight)
    if max(nums_counter.values()) == 3:
        t = []
        for n in nums:
            if nums_counter[n] == 3:
                n1 = n
            else:
                t.append(n)
        return (THREE_OF_A_KIND, tuple([n1]+t))
    if max(nums_counter.values()) == 2:
        if len(set(nums)) == 3:
            t = set()
            for n in nums:
                if nums_counter[n] == 2:
                    t.add(n)
                else:
                    n3 = n
            return (TWO_PAIR, tuple(sorted(t, reverse=True)+[n3]))
        else:
            t = []
            for n in nums:
                if nums_counter[n] == 2:
                    n1 = n
                else:
                    t.append(n)
            return (ONE_PAIR, tuple([n1]+sorted(t, reverse=True)))
    return (HIGH_CARD, tuple(sorted(nums, reverse=True)))


def best_hands(hands):
    r = [[], (-1, tuple())]
    for hand in hands:
        p, t = check_hand(hand)
        if p > r[1][0] or (p == r[1][0] and t > r[1][1]):
            r = [[hand], (p, t)]
        elif p == r[1][0] and t == r[1][1]:
            r[0].append(hand)
    return r[0]
