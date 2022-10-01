def primes(limit):
    # defines an empty list of prime numebers and range of possible ones
    prime_lst = []
    num_lst = list(range(2, limit + 1))

    # loops num_lst until there are no more possible numbers
    while len(num_lst):
        # the first num of the list is prime
        prime_lst.append(num_lst[0])
        # creates a list with candidates that are multiples of the first number
        initial_num = num_lst[0]
        candidates = [initial_num]
        num = 1
        while candidates[-1] <= limit:
            candidates.append(initial_num * num)
            num += 1
        # loops the candidates and removes the ones that are in the num_lst
        for can in candidates:
            if can in num_lst:
                num_lst.remove(can)
    # returns the list of prime numbers
    return prime_lst
