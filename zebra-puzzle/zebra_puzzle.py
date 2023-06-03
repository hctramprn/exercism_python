from itertools import permutations

people = ['Norwegian', 'Spaniard', 'Ukrainian', 'Englishman', 'Japanese']


def get_nationality():

    g = ((water, zebra) for (red, green, ivory, yellow, blue) in permutations(range(5)) if green - ivory == 1 for (norway, spain, ukraine, english, japan) in permutations(range(5)) if norway == 0 if english == red for (dog, fox, snails, horse, zebra) in permutations(range(5)) if spain == dog for (coffee, tea, milk, orange, water)
         in permutations(range(5)) if milk == 2 if coffee == green if ukraine == tea for (oldgold, kools, chesterfields, luckystrike, parliaments) in permutations(range(5)) if oldgold == snails if kools == yellow if chesterfields - fox == 1 if horse - kools == 1 if luckystrike == orange if parliaments == japan if blue - norway == 1)

    return next(g)


def drinks_water():
    water, _ = get_nationality()
    return people[water]


def owns_zebra():
    _, zebra = get_nationality()
    return people[zebra]
