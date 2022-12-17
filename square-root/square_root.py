def square_root(number):

    num = number
    sol = 1

    while sol <= num:
        if sol**2 == num:
            return sol
        sol += 1
