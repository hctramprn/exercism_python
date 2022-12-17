from itertools import combinations_with_replacement as comb_rep


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    checkError(min_factor, max_factor)
    combination_iter_rev = iter(
        comb_rep(range(max_factor, min_factor - 1, -1), 2))
    combination_gen_rev = pal_gen(combination_iter_rev)
    
    if combination_gen_rev[0] == None:
        return combination_gen_rev

    sorted_list = sorted(combination_gen_rev, reverse=True)
    value = sorted_list[0][0]
    factors = [g for _, g in sorted_list if g[0] * g[1] == value]
    return value, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    checkError(min_factor, max_factor)
    combination_iter = iter(comb_rep(range(min_factor, max_factor + 1), 2))
    combination_gen = pal_gen(combination_iter)

    if combination_gen[0] == None:
        return combination_gen

    sorted_list = sorted(combination_gen, reverse=False)

    value = sorted_list[0][0]
    factors = [g for _, g in sorted_list if g[0] * g[1] == value]
    return value, factors


def pal_gen(combination):
    pal_lst = []
    while True:

        try:
            x, y = next(combination)
        except StopIteration:
            return (None, [])

        if len(pal_lst) > 10:
            break
        if str((x * y)) == str((x * y))[::-1]:
            pal_lst.append((x * y, [x, y]))
    return pal_lst


def checkError(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
