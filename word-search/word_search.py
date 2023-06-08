class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        possible_starting_points = []
        
        # Find possible starting points for the word in the puzzle
        for i in range(len(self.puzzle[0])):
            for j in range(len(self.puzzle)):
                if self.puzzle[j][i] == word[0]:
                    possible_starting_points.append((i, j))

        # Check for word matches in different directions from each starting point
        for candidate in possible_starting_points:
            x1, y1 = candidate
            x_max = len(self.puzzle[0])
            y_max = len(self.puzzle)
            difference = len(word) - 1

            # Check left to right
            if (x1 + difference) < x_max:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1][x1 + k]
                if match == word:
                    return Point(x1, y1), Point(x1 + difference, y1)

            # Check bottom left to top right
            if (x1 + difference) < x_max and (y1 - difference) >= 0:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1 - k][x1 + k]
                if match == word:
                    return Point(x1, y1), Point(x1 + difference, y1 - difference)

            # Check bottom to top
            if (y1 - difference) >= 0:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1 - k][x1]
                if match == word:
                    return Point(x1, y1), Point(x1, y1 - difference)

            # Check bottom right to top left
            if (x1 - difference) >= 0 and (y1 - difference) >= 0:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1 - k][x1 - k]
                if match == word:
                    return Point(x1, y1), Point(x1 - difference, y1 - difference)

            # Check right to left
            if (x1 - difference) >= 0:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1][x1 - k]
                if match == word:
                    return Point(x1, y1), Point(x1 - difference, y1)

            # Check top right to bottom left
            if (x1 - difference) >= 0 and (y1 + difference) < y_max:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1 + k][x1 - k]
                if match == word:
                    return Point(x1, y1), Point(x1 - difference, y1 + difference)

            # Check top to bottom
            if (y1 + difference) < y_max:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1 + k][x1]
                if match == word:
                    return Point(x1, y1), Point(x1, y1 + difference)

            # Check top left to bottom right
            if (x1 + difference) < x_max and (y1 + difference) < y_max:
                match = ''
                for k in range(len(word)):
                    match += self.puzzle[y1 + k][x1 + k]
                if match == word:
                    return Point(x1, y1), Point(x1 + difference, y1 + difference)
        
        # If no match is found, return None
        return None


