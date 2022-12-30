def spiral_matrix(size):
    # defines an empty matrix that will hold the spiral
    matrix = [[None] * size for _ in range(size)]
    # sets a list of numbers for each position
    numbers = list(range((size**2), 0, -1))

    # defines the boundaries of the matrix
    min_h = 0
    max_h = size - 1
    min_v = 0
    max_v = size - 1

    # sets the direction of the movement
    up = False
    down = False
    right = True
    left = False

    # sets the position in the matrix where the code
    # is going to change the value
    position = 0

    '''Loop that changes each value in the matrix depending
    on the direction of the movement.

    If the position is in range, changes the value in the matrix 
    and advances to the next position. Then it updates the numbers 
    list by removing the last item.

    Else, if the position is out of range, changes the direction 
    of the movement and updates the matrix's boundaries.
    '''
    while numbers:
        if right:
            if position <= max_h:
                matrix[min_v][position] = numbers[-1]
                position += 1
                numbers.pop()
            else:
                right = False
                down = True
                min_v += 1
                position = min_v
        if down:
            if position <= max_v:
                matrix[position][max_h] = numbers[-1]
                position += 1
                numbers.pop()
            else:
                down = False
                left = True
                max_h -= 1
                position = max_h
        if left:
            if min_h <= position:
                matrix[max_v][position] = numbers[-1]
                position -= 1
                numbers.pop()
            else:
                left = False
                up = True
                max_v -= 1
                position = max_v
        if up:
            if min_v <= position:
                matrix[position][min_h] = numbers[-1]
                position -= 1
                numbers.pop()
            else:
                up = False
                right = True
                min_h += 1
                position = min_h

    # returns the matrix
    return matrix
