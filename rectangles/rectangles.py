def rectangles(strings):
    # find vertices
    vertices = []
    for line in strings:
        line_ver_temp = []
        for i in range(len(line)):
            if line[i] == '+':
                line_ver_temp.append(i)
        vertices.append(line_ver_temp)
    # print(vertices)

    # find possible square sides
    sides_possible = []
    for ver_sublist in vertices:
        index = 0
        for ver in ver_sublist:
            for j in range(len(ver_sublist)):
                if ver_sublist[j] - ver_sublist[index] > 0:
                    sides_possible.append((ver_sublist[index], ver_sublist[j]))
            index += 1

    # find the combinations of sides
    combinations_per_side = [sides_possible.count(v) - 1 for v in set(sides_possible)]
    rectangles = 0
    for num in combinations_per_side:
        for n in range(num + 1):
            rectangles += n
    return rectangles