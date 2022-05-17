def equilateral(sides):
    a, b, c = sides
    if (a + b + c) > 0:
        return a == b == c
    return False


def isosceles(sides):
    a, b, _ = sorted(sides, reverse=True)
    return a == b


def scalene(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a != b != c
    return False
