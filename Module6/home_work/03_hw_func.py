def circles_inside(x1, y1, R1, x2, y2, R2):
    distance_centers = distance((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if distance_centers + R2 <= R1:
        return True
    elif distance_centers + R1 <= R2:
        return True
    else:
        return False
