from audioop import mul


def sum_of_multiples(limit, multiples):
    multiples_list = []
    for mult in multiples:
        if mult > 0:
            for num in range(limit):
                if num % mult == 0:
                    multiples_list.append(num)
    return sum(set(multiples_list))
