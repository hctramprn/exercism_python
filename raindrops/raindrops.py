def convert(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    num = ''
    for f in factors:
        if number % f == 0:
            num += factors[f]

    if len(num) == 0:
        num = str(number)

    return num
