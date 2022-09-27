# Globals for the directions
# Change the values as you see fit
NORTH = {'name': 'NORTH', 'L': 'WEST', 'R': 'EAST', 'x': 0, 'y': 1}
EAST = {'name': 'EAST', 'L': 'NORTH', 'R': 'SOUTH', 'x': 1, 'y': 0}
SOUTH = {'name': 'SOUTH', 'L': 'EAST', 'R': 'WEST', 'x': 0, 'y': -1}
WEST = {'name': 'WEST', 'L': 'SOUTH', 'R': 'NORTH', 'x': -1, 'y': 0}


class Robot:
    # declares initial direction and position
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    # initialize the movement of the robot
    def move(self, instructions):
        # get local position and direction
        x_temp, y_temp = self.coordinates
        dir_temp = self.direction

        # loops through the instructions and updates position and directions using global dictionaries
        for char in instructions:
            if char == 'A':
                x_temp += dir_temp['x']
                y_temp += dir_temp['y']
            else:
                dir_temp = eval(dir_temp[char])

        # updates Robot's position and direction
        self.coordinates = (x_temp, y_temp)
        self.direction = eval(dir_temp['name'])
