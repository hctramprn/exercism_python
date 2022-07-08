def factors(value):
    """Function that returns the prime factors of a given value.

    :param value: int - Value that will be decomposed into its prime factors
    :return: lst - List of prime factors

    This function returns a list of prime factors for a given value.

    """

    # sets an empty list for the prime factors
    factors_lst = []
    num = 2

    # test if the number is not a prime factor
    while num <= value:
        if value % num == 0:
            factors_lst.append(num)
            value = value / num
        else:
            num += 1
    # returns a list with the prime factors
    return factors_lst
