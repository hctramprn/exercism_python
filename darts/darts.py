def score(x, y):
    center_distance = ((x**2)+(y**2))**0.5
    if center_distance <= 10:
        if center_distance <= 5:
            if center_distance <= 1:
                return 10
            return 5
        return 1
    return 0
