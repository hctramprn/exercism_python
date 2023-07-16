import itertools

def can_chain(dominoes):
    # Empty list is returned if the dominoes list is empty
    if not dominoes:
        return []

    # Create a list of all possible combinations of each domino and its reverse
    all_combinations = [(dom, tuple(reversed(dom))) for dom in dominoes]

    try:
        match = next(find_combination(all_combinations, dominoes))
    except StopIteration:
        # Return None if no valid combination is found
        return None

    return list(match)


def find_combination(all_combinations, dominoes):
    all_orders = itertools.permutations(all_combinations, len(dominoes))

    for perm in all_orders:
        cartesian_product = itertools.product(*perm)

        for combination in cartesian_product:
            # Check if the first and last dominoes can be chained together
            if combination[0][0] == combination[-1][1]:
                is_ordered = [combination[i - 1][1] == combination[i][0] for i in range(1, len(combination))]
                # Check if all subsequent dominoes can be chained with the previous one
                if all(is_ordered):
                    # Yield the valid combination
                    yield combination
