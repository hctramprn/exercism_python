
class ConnectGame:
    def __init__(self, board):
        # defines each set of coordinates
        self.x_positions = set()
        self.o_positions = set()
        # process the board and gets the coordinates of X and O
        self.lines = self.board_split(board)
        # defines the starting and ending coordinates of X and O
        self.x_start = set(
            [coord for coord in self.x_positions if coord[1] == 0])
        self.x_end = set(
            [coord for coord in self.x_positions if coord[1] == len(self.lines[0]) - 1])
        self.o_start = set(
            [coord for coord in self.o_positions if coord[0] == 0])
        self.o_end = set(
            [coord for coord in self.o_positions if coord[0] == len(self.lines) - 1])

    # function that gets the coordinates of each character
    def board_split(self, board):
        split = board.split('\n')
        lines = [line.lstrip() for line in split]
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == 'X':
                    self.x_positions.add((i, j))
                elif lines[i][j] == 'O':
                    self.o_positions.add((i, j))
        return lines

    # obtain the winner of the board
    def get_winner(self):
        # if there are starting and ending coordinates, test for X
        if self.x_start and self.x_end:
            # loop that checks if possible neighbor nodes are present
            x_path = self.x_start
            new_additions = self.x_start
            while new_additions:
                possible_nodes = set()
                for coord in new_additions:
                    upper = [(coord[0] - 1, coord[1]),
                             (coord[0] - 1, coord[1] + 2)]
                    side = [(coord[0], coord[1] - 2), (coord[0], coord[1] + 2)]
                    lower = [(coord[0] + 1, coord[1] - 2),
                             (coord[0] + 1, coord[1])]
                    possible_nodes.update(upper, side, lower)

                # set new_additions to all the possible coordinates
                # that are in x_positions and not in x_path
                new_additions = (self.x_positions.intersection(
                    possible_nodes)).difference(x_path)
                # updates the x_path
                x_path.update(new_additions)
                if x_path.intersection(self.x_end):
                    return 'X'

        # if there are starting and ending coordinates, test for O
        if self.o_start and self.o_end:
            # loop that checks if possible neighbor nodes are present
            o_path = self.o_start
            new_additions = self.o_start
            while new_additions:
                possible_nodes = set()
                for coord in new_additions:
                    upper = [(coord[0] - 1, coord[1]),
                             (coord[0] - 1, coord[1] + 2)]
                    side = [(coord[0], coord[1] - 2), (coord[0], coord[1] + 2)]
                    lower = [(coord[0] + 1, coord[1] - 2),
                             (coord[0] + 1, coord[1])]
                    possible_nodes.update(upper, side, lower)

                # set new_additions to all the possible coordinates
                # that are in o_positions and not in o_path
                new_additions = (self.o_positions.intersection(
                    possible_nodes)).difference(o_path)
                # updates the x_path
                o_path.update(new_additions)
                if o_path.intersection(self.o_end):
                    return 'O'

        # if there are not starting and ending coordinates
        # for neither X and O, returns a non winner status
        return ''
