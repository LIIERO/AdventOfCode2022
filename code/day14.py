
def main():
    data = txt_into_array()
    data = [[tuple([int(p) for p in p.split(',')]) for p in el.split(' -> ')] for el in data]
    rang = max([max([el[1] for el in line]) for line in data]) + 1
    area = [['.']*1000 for _ in range(rang)]
    for line in data:
        x, y = line[0]
        for point in line[1:]:
            if x == point[0]:
                if y < point[1] + 1: p1, p2 = y, point[1] + 1
                else: p1, p2 = point[1], y + 1
                for i in range(p1, p2): area[i][x] = '#'
            if y == point[1]:
                if x < point[0] + 1: p1, p2 = x, point[0] + 1
                else: p1, p2 = point[0], x + 1
                for i in range(p1, p2): area[y][i] = '#'
            x, y = point
    area[0][500] = '+'

    area = area + [['.']*1000, ['#']*1000]

    no_units = 0
    done = False
    while not done:
        sand_y, sand_x = 0, 500  # spawn
        can_move = True
        while can_move:
            new_y = sand_y + 1
            '''if new_y == rang:
                done = True
                break'''

            if area[new_y][sand_x] == '.':
                sand_y = new_y
            elif area[new_y][sand_x - 1] == '.':
                sand_y = new_y
                sand_x = sand_x - 1
            elif area[new_y][sand_x + 1] == '.':
                sand_y = new_y
                sand_x = sand_x + 1
            else:
                area[sand_y][sand_x] = 'o'
                no_units += 1
                can_move = False
                if area[0][500] == 'o':
                    done = True
                    break

    for row in area:
        print(row)

    print(no_units)

