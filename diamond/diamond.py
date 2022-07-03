import string

ABC = string.ascii_uppercase


def rows(letter):
    # defines the initial array and its padding size
    str = []
    padding = ((ABC.index(letter) + 1) * 2) - 1

    # loops through the alphabet characters and space them with the correct sequence
    for char in ABC[:ABC.index(letter) + 1]:
        if char != 'A':
            index = ABC.index(char)
            inner = char + (' ' * 2 * index)[1:] + char
        else:
            inner = 'A'

        # adds the padding to the spaced characters
        centered = inner.center(padding, ' ')
        str.append(centered)

    # adds the other half of the diamond and returns the array
    str += reversed(str[:-1])
    return str
