def rectangles(strings):
    # find all the vertices
    vertices_coordinates = []
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == '+':
                vertices_coordinates.append((j, i))
    # print(vertices_coordinates)

    # validate each possible rectangle
    possible_rectangles = []
    # starting coordinates 1
    for first_coordinate in vertices_coordinates:
        x1, y1 = first_coordinate[0], first_coordinate[1]
        # test each of the other coordinates in the list
        for second_coordinate in vertices_coordinates:
            if first_coordinate != second_coordinate:
                x2, y2 = second_coordinate[0], second_coordinate[1]
                # checks if the 4 possible vertices exist in the list and appends them
                vertices_temp = set(((x1, y1), (x1, y2), (x2, y2), (x2, y1)))
                if len(vertices_temp) == 4 and vertices_temp.issubset(set(vertices_coordinates)) and vertices_temp not in possible_rectangles:
                    possible_rectangles.append(vertices_temp)

    # test each of the possible rectangles
    rectangles = 0
    for rectangle_set in possible_rectangles:
        lenght_x = set([x[0] for x in rectangle_set])
        lenght_y = set([x[1] for x in rectangle_set])
        
        # test horizontals
        tested_sides = 0
        for row in lenght_y:
            if set(strings[row][min(lenght_x):max(lenght_x) + 1]).issubset('+-'):
                tested_sides += 1
        
        # test verticals
        for column in lenght_x:
            col_temp = ''
            for row in range(min(lenght_y), max(lenght_y) + 1):
                col_temp += strings[row][column]
            if set(col_temp).issubset('+|'):
                tested_sides += 1

        # check sides
        if tested_sides == 4:
            rectangles += 1
    
    return rectangles