class Queen:
    """Class that creates a chess queen object.

    :param row: int - The row in which the queen will be.
    :param column: int - The column in which the queen will be.
    """
    # Init the class with passed row and column values
    def __init__(self, row, column):
        self.row = self.row_validation(row)
        self.column = self.column_validation(column)
    
    # Returns bool if a queen can attack and is not in the same space as the other queen
    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        return abs(self.row - another_queen.row) == abs(self.column - another_queen.column) or self.row == another_queen.row or self.column == another_queen.column

    # Checks if the queen is in a valid row on the board
    def row_validation(self, row):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        return row

    # Checks if the queen is in a valid column on the board
    def column_validation(self, column):
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        return column
