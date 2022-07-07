def transpose(lines):
    # defines the size of the matrix
    lines = lines.split('\n')
    columns = len(lines)
    rows = max([len(element) for element in lines])

    # creates an empty list and loops through the elements by each index
    transposed = []
    for i in range(rows):
        word = ''
        for j in range(columns):
            # tries to access each string by index. If the string is out of index adds a space ' '
            try:
                # replace each space with @ sign to avoid rstrip() method removes string spaces
                if lines[j][i] == ' ':
                    word += '@'
                else:
                    word += lines[j][i]
            except:
                word += ' '
        # appends each word to the matrix list
        transposed.append(word.rstrip().replace('@', ' '))
    return '\n'.join(transposed)
