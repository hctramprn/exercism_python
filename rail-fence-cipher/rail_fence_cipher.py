def encode(message, rails):
    # declares the rows for each rail
    rows = ['' for _ in range(rails)]
    row = 0

    # loop that assigns each character to the corresponding rail
    for i in range(len(message)):
        rows[row] += message[i]
        
        # changes the direction of the loop
        if row == (rails - 1):
            direction = -1
        elif row == 0:
            direction = 1
        row += direction

    # returns the joined list that represents the encoded message
    return ''.join(rows)


def decode(encoded_message, rails):
    # declares the rows for each rail
    rows = [[] for _ in range(rails)]
    row = 0

    # loop that assigns each character to the corresponding rail
    for i in range(len(encoded_message)):
        rows[row].append(i)

        # changes the direction of the loop
        if row == (rails - 1):
            direction = -1
        elif row == 0:
            direction = 1
        row += direction

    # flattens the nested lists
    flat_list = [num for sublist in rows for num in sublist]

    # creates a list of tuples containing the positions of each character
    positions_list = [(flat_list[i], encoded_message[i])
                      for i in range(len(encoded_message))]

    # sorts the list and extracts the characters of the message
    sorted_list = [coord[1] for coord in sorted(positions_list)]

    # returns the joined list that represents the decoded message
    return ''.join(sorted_list)
