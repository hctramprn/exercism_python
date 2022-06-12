from asyncore import loop


def prime(number):
    """Function that returns the nth prime number.

    :param number: int - nth prime number.
    :return: int - the prime number in the nth position.

    This function returns the prime number in the nth asked position. It raises an error in case the zeroth prime is asked.
    """

    if not number:
        raise ValueError('there is no zeroth prime')

    goal = number
    num = 3
    primes = [2]

    while len(primes) < goal:
        for p in primes:
            if num % p == 0:
                break
            if p == primes[-1]:
                primes.append(num)
        num += 2
    return primes[-1]
