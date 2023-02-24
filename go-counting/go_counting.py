BLACK = 'BLACK'
WHITE = 'WHITE'
NONE = 'NONE'


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.height = len(board)
        self.width = len(board[0])
        self.groups = self.get_groups(board)

    def get_groups(self, board):
        # loop that gets the coordinates of the blanks
        blanks = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ' ':
                    blanks.add((j, i))


        # groups the blank coordinates in sets
        groups = []
        # while there are blanks without grouping
        while blanks:
            # creates a set with the first coordinate available
            subgroup = set()
            subgroup.add(list(blanks)[0])

            step_coordinates = subgroup.copy()
            # test for new members of the group
            new_members = True
            while new_members:
                # loop that get the adjacent coordinates
                temp_coord = set()
                for x, y in step_coordinates:
                    adjacent_coords = {
                        (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
                    temp_coord.update(adjacent_coords)

                # if no adjacent coordinates left in the set blanks, stop searching
                if temp_coord.isdisjoint(blanks):
                    new_members = False
                # else, get all the intersections and update the subgroup set
                else:
                    temp_coord.intersection_update(blanks)
                    subgroup = subgroup.union(temp_coord)

                    # takes the new members to only test them in the next iteration for efficency
                    step_coordinates = temp_coord.copy()
                # removes all the coordinates in blanks that are already grouped
                blanks.difference_update(subgroup)
            # appends the subgroup to the group list
            groups.append(subgroup)
        #creates the list that will become the dictionary of territories
        players = [[NONE, list()], [WHITE, list()], [BLACK, list()]]
        # loops that finds if there a multiple colors as neighbors cells
        for group in groups:
            test_string = ''
            for x, y in group:
                try:
                    up = board[y - 1][x]
                except IndexError:
                    up = ''
                try:
                    down = board[y + 1][x]
                except IndexError:
                    down = ''
                try:
                    left = board[y][x - 1]
                except IndexError:
                    left = ''
                try:
                    right = board[y][x + 1]
                except IndexError:
                    right = ''

                test_string += up + down + left + right

            membership = set(test_string.replace(' ', ''))
            if len(membership) > 1:
                players[0][1].append(group)
            elif 'W' in membership:
                players[1][1].append(group)
            elif 'B' in membership:
                players[2][1].append(group)

        # if the dictionary has no values, add an initial coordinate
        if len(players[0][1]) + len(players[1][1]) + len(players[2][1]) == 0:
            players[0][1].append({(0, 0)})

        return dict(players)

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """

        if 0 <= x < self.width and 0 <= y < self.height:
            for color, subgroups in self.groups.items():
                for coordinates in subgroups:
                    if (x, y) in coordinates:
                        return (color, coordinates)
            return (NONE, set())
        else:
            raise ValueError('Invalid coordinate')

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        print(self.groups)
        territories_lst = []
        for color, subgroups in self.groups.items():
            temp_lst = []
            for coordinates in subgroups:
                temp_lst.extend(list(coordinates))
            territories_lst.append((color, set(temp_lst)))
        return dict(territories_lst)
