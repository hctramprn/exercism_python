ROMANS = {'1': ('I', 'X', 'C', 'M'), '2': ('II', 'XX', 'CC', 'MM'), '3': ('III', 'XXX', 'CCC', 'MMM'), '4': ('IV', 'XL', 'CD'), '5': (
    'V', 'L', 'D'), '6': ('VI', 'LX', 'DC'), '7': ('VII', 'LXX', 'DCC'), '8': ('VIII', 'LXXX', 'DCCC'), '9': ('IX', 'XC', 'CM')}


def roman(number):
    # creates an empty list and reverse the list of string that represents the number
    romans_lst = []
    num = list(str(number))[::-1]

    # loops through the list of numbers and asign the correct roman number depending on the position
    for i in range(len(num)):
        if num[i] != '0':
            romans_lst.append(ROMANS[num[i]][i])

    # returns a joined list of roman numbers
    return ''.join(reversed(romans_lst))
