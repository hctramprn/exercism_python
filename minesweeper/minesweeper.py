

def annotate(minefield):
    # returns the same board if it is empty
    try:
        minefield[0][0]
    except:
        return minefield

    # raise a ValueError exception if the board is invalid
    # if rows are unequal
    lens = set([len(row) for row in minefield])
    # if there are strange characters
    chars = [c.difference({'*',' '}) for c in [set(row) for row in minefield]]
    strange_chars = [s for s in chars if s != set()]
    # checks conditions and raises error if one is met
    if len(strange_chars) > 0 or len(lens) > 1:
        raise ValueError("The board is invalid with current input.")

    # maps the board and gets the mines' coordinates
    mines_map = set()
    for i in range(len(minefield)):
        for j in range(len(minefield[i])):
            if minefield[i][j] == '*':
                mines_map.add((i, j))

    # inits the list that will contain each row
    mine_counter = []
    # loops each row
    for i in range(len(minefield)):
        row = ''
        # loops each char in row
        for j in range(len(minefield[i])):
            # if the char is a blank space
            if minefield[i][j] == ' ':
                # init the coordinates for the possible surrounding mines
                surrounding_mines = set()
                top = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]
                sides = [(i, j - 1), (i, j + 1)]
                bottom = [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
                surrounding_mines.update(top, sides, bottom)
                # if mines are present, count them and append that number
                if len(surrounding_mines.intersection(mines_map)) > 0:
                    mines_found = str(
                        len(surrounding_mines.intersection(mines_map)))
                # else, leves the char as it is
                else:
                    mines_found = ' '
                # appends the mines result to the row
                row += mines_found
            #else, leaves the char as it is
            else:
                row += '*'
        # appends the new row to the mine_counter list and returns it
        mine_counter.append(row)
    
    return mine_counter