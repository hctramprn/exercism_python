def steps(number):
    """Function that returns the number of steps required to reach 1 in the collatz conjecture.

    :param number: int - starting number in the conjecture.

    The function should return the number of steps required to reach 1 given an initial number for the collatz conjecture.

    """
    if not number > 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    num = number
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        steps += 1
    return steps
