def rows(row_count, triangle=[]):
    # This is someone else solution in order to complete this exercise
    if row_count < 0:
        raise ValueError('number of rows is negative')

    if row_count == 0:
        return []

    if row_count == 1:
        return [[1]]

    triangle = rows(row_count-1)

    prev_row = [0] + list(triangle[-1:][0]) + [0]

    triangle.append([sum(prev_row[i:i+2]) for i in range(0, row_count)])
    return triangle