def distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

dic = { 'AB':0, 'BC':0, 'AC':0 }

point_a = (2, 3)
point_b = (7, -3)
point_c = (5, 1)

dic['AB'] = distance(*point_a, *point_b)
dic['BC'] = distance(*point_b, *point_c)
dic['AC'] = distance(*point_a, *point_c)

min_dist = min(dic.values())
for key, value in dic.items():
    if value == min_dist:
        print("Самый короткий отрезок:", key)
        break
