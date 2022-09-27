def saddle_points(matrix):
    # evaluates for empty or irregular matrix
    matrix_len = len(set([len(row) for row in matrix]))
    if matrix_len > 1:
        raise ValueError("irregular matrix")
    elif matrix_len == 0:
        return []

    # construct a list with the columns sublists
    columns = []
    for i in range(len(matrix[0])):
        column_temp = []
        for j in range(len(matrix)):
            column_temp.append(matrix[j][i])
        columns.append(column_temp)
    
    # evaluare for saddle points criteria
    saddles = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(columns[j]):
                saddles.append({"row": i + 1, "column": j + 1})
    return saddles
