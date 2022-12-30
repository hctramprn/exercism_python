def rebase(input_base, digits, output_base):
    # raises ValueErrors if the input or output bases are less than 2
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')

    # loops through the digits to convert the number to base 10
    base10_num = 0
    position = len(digits) - 1
    for d in digits:
        # raises an error if a digit is out of range
        if not 0 <= d < input_base:
            raise ValueError('all digits must satisfy 0 <= d < input base')

        base10_num += (d * (input_base ** position))
        position -= 1

    # indefinite loop that holds all the remainders
    remainder_lst = []
    while base10_num:
        rem = base10_num % output_base
        remainder_lst.append(rem)
        base10_num = base10_num // output_base

    # if the output is an empty list, return [0]
    # else, returns the list reversed
    if not remainder_lst:
        return [0]
    else:
        return remainder_lst[::-1]
