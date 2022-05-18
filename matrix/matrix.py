class Matrix:
    def __init__(self, matrix_string):
        self.matrix_rows = [[int(r) for r in row.split(' ')]
                            for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix_rows[index - 1]

    def column(self, index):
        column_list = []
        for row in self.matrix_rows:
            column_list.append(row[index - 1])
        return column_list
