
def triplets_with_sum(number):
    # someone else solution
    result = []
    for a in range(1, number//3):
        for b in range(max(a+1, number//2-a-1), (number-a)//2+1):
            partial = a*a + b*b
            c = number-a-b
            if partial == c*c:
                result.append([a, b, c])
    return result
