
def main():
    data = [[int(val) for val in el.split(',')] for el in txt_into_array()]
    sides = 6 * len(data)
    print(sides)

    area_size = 20
    area = [[['.']*area_size for l in range(area_size)] for k in range(area_size)]
    for cube in data:
        area[cube[0]][cube[1]][cube[2]] = '#' # z, y, x

    # print(data)
    prev_layer = [['.']*area_size]*area_size
    for z, layer in enumerate(area):
        # print(z)
        prev_row = ['.']*area_size
        for y, row in enumerate(layer):
            # print(row)
            prev_el = '.'
            for x, el in enumerate(row):
                if prev_el == '#' and el == '#': sides -= 2
                if prev_row[x] == '#' and row[x] == '#': sides -= 2
                if prev_layer[y][x] == '#' and layer[y][x] == '#': sides -= 2

                prev_el = el
            prev_row = row
        prev_layer = layer

    print(sides)

# Część 2

import sys
sys.setrecursionlimit(2000)

def pour_water(area, p, depth, b):
    area[p[0]][p[1]][p[2]] = 'o'
    f = ['o', '#']
    if depth < 1900:
        if p[0] > b[0][0] and area[p[0] - 1][p[1]][p[2]] not in f: pour_water(area, [p[0] - 1, p[1], p[2]], depth + 1, b)
        if p[0] < b[0][1] and area[p[0] + 1][p[1]][p[2]] not in f: pour_water(area, [p[0] + 1, p[1], p[2]], depth + 1, b)
        if p[1] > b[1][0] and area[p[0]][p[1] - 1][p[2]] not in f: pour_water(area, [p[0], p[1] - 1, p[2]], depth + 1, b)
        if p[1] < b[1][1] and area[p[0]][p[1] + 1][p[2]] not in f: pour_water(area, [p[0], p[1] + 1, p[2]], depth + 1, b)
        if p[2] > b[2][0] and area[p[0]][p[1]][p[2] - 1] not in f: pour_water(area, [p[0], p[1], p[2] - 1], depth + 1, b)
        if p[2] < b[2][1] and area[p[0]][p[1]][p[2] + 1] not in f: pour_water(area, [p[0], p[1], p[2] + 1], depth + 1, b)
    # else: print('Depth exceeded')

def main():
    data = [[int(val) for val in el.split(',')] for el in txt_into_array()]
    sides = 0

    area_size = 22 # 20
    area = [[['.']*area_size for l in range(area_size)] for k in range(area_size)]
    for cube in data:
        area[cube[0] + 1][cube[1] + 1][cube[2] + 1] = '#' # z, y, x

    l_p = area_size - 1
    h_p = area_size//2
    s_m, m_e = (0, h_p), (h_p, l_p)
    pour_water(area, [0, 0, 0], 0, (s_m, s_m, s_m))
    pour_water(area, [l_p, 0, 0], 0, (m_e, s_m, s_m))
    pour_water(area, [0, l_p, 0], 0, (s_m, m_e, s_m))
    pour_water(area, [0, 0, l_p], 0, (s_m, s_m, m_e))
    pour_water(area, [l_p, l_p, 0], 0, (m_e, m_e, s_m))
    pour_water(area, [0, l_p, l_p], 0, (s_m, m_e, m_e))
    pour_water(area, [l_p, 0, l_p], 0, (m_e, s_m, m_e))
    pour_water(area, [l_p, l_p, l_p], 0, (m_e, m_e, m_e))


    # print(data)
    prev_layer = [['.']*area_size]*area_size
    for z, layer in enumerate(area):
        # print(z)
        prev_row = ['.']*area_size
        for y, row in enumerate(layer):
            # print(row)
            prev_el = '.'
            for x, el in enumerate(row):
                if (prev_el == 'o' and el == '#') or (prev_el == '#' and el == 'o'): sides += 1
                if (prev_row[x] == 'o' and row[x] == '#') or (prev_row[x] == '#' and row[x] == 'o'): sides += 1
                if (prev_layer[y][x] == 'o' and layer[y][x] == '#') or (prev_layer[y][x] == '#' and layer[y][x] == 'o'): sides += 1

                prev_el = el
            prev_row = row
        prev_layer = layer

    print(sides)

