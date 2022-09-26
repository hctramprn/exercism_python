ranks = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}


hands_rank = []
suits = []
pips = []
high_card_rank = []

def best_hands(hands):
    hands_norm = [h.split() for h in hands]
    # get the suits and pips of each hand
    # loops through the sublists
    for hand in hands_norm:
        temp_list_suits = []
        temp_list_pips = []
        # get the suit and pip of each card in the sublist
        for s in hand:
            temp_list_suits.append(s[-1])
            temp_list_pips.append(ranks[s[:-1]])
        # appends each sublist of suits and pips to a general list
        suits.append(temp_list_suits)
        pips.append(temp_list_pips)

    # evaluates each hand and assigns them a rank
    for i in range(len(hands_norm)):
        high_card_rank.append(high_card(pips[i]))
        if straight_flush(suits[i], pips[i]):
            hands_rank.append(2)
            continue
        if four_of_a_kind(pips[i]):
            hands_rank.append(3)
            continue
        if full_house(pips[i]):
            hands_rank.append(4)
            continue
        if flush(suits[i]):
            hands_rank.append(5)
            continue
        if straight(pips[i]):
            hands_rank.append(6)
            continue
        if three_of_a_kind(pips[i]):
            hands_rank.append(7)
            continue
        if two_pair(pips[i]):
            hands_rank.append(8)
            continue
        if one_pair(pips[i]):
            hands_rank.append(9)
            continue
        else:
            hands_rank.append(10)

    possible_winners = []
    highest_rank = 0
    for i in range(len(hands)):
        if hands_rank[i] == min(hands_rank):
            possible_winners.append([hands[i], high_card_rank[i]])
            if high_card_rank[i] > highest_rank:
                highest_rank = high_card_rank[i]

    winners = [hand[0] for hand in possible_winners if hand[1] == highest_rank]
    # print(hands_rank, high_card_rank, winners)
    return winners



# finds if the hand has only one type of suit and the pips are in a range of 5
def straight_flush(suits, pips):
    suit_set = set(suits)
    pip_set = set(pips)
    if len(suit_set) == 1 and pip_set.issubset(set(range(min(pip_set), min(pip_set) + 5))):
        return True


# returns True if the hand has two types of suits and a pip is repeated 4 times
def four_of_a_kind(pips):
    pip_set = set(pips)
    pip_count = []
    for num in pip_set:
        pip_count.append(pips.count(num))
    if len(pip_set) == 2 and 4 in pip_count:
        return True


# returns True if the hand has two types of suits and a pip is repeated 3 times
def full_house(pips):
    pip_set = set(pips)
    pip_count = []
    for num in pip_set:
        pip_count.append(pips.count(num))
    if len(pip_set) == 2 and 3 in pip_count:
        return True


# returns True if the hand has only one type of suit
def flush(suits):
    suit_set = set(suits)
    if len(suit_set) == 1:
        return True


# returns True is the hand's pips are in a range of 5
def straight(pips):
    pip_set = set(pips)
    if len(pip_set) == 5 and pip_set.issubset(set(range(min(pip_set), min(pip_set) + 5))):
        return True


# returns True if a pip is repeated three times
def three_of_a_kind(pips):
    pip_set = set(pips)
    pip_count = []
    for num in pip_set:
        pip_count.append(pips.count(num))
    if len(pip_set) == 3 and 3 in pip_count:
        return True


# returns True if a pip is repeated two times
def two_pair(pips):
    pip_set = set(pips)
    pip_count = []
    for num in pip_set:
        pip_count.append(pips.count(num))
    if len(pip_set) == 3 and 2 in pip_count:
        return True


# returns True if a pip is repeated two times
def one_pair(pips):
    pip_set = set(pips)
    pip_count = []
    for num in pip_set:
        pip_count.append(pips.count(num))
    if len(pip_set) == 4 and 2 in pip_count:
        return True


# returns True if a pip is repeated two times
def high_card(pips):
    return max(pips)