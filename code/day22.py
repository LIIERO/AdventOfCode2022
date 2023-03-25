
def main():
    data = txt_into_array_raw()
    path_d = data[-1]
    area = data[:-2]
    path_d = path_d.split('R')
    path = [int(path_d[0])]
    for el in path_d[1:]:
        path.append('R')
        el = el.split('L')
        new_el = [int(el[0])]
        for val in el[1:]: new_el += ['L', int(val)]
        path += new_el

    min_max_ind_list = []
    for j, row in enumerate(area):
        area[j] = list(area[j])
        print(row)
        i = 0
        while row[i] == ' ': i += 1
        min_max_ind_list.append((i, len(row) - 1))
    print(path)
    print(min_max_ind_list)
    max_ind = len(min_max_ind_list) - 1
    print(max_ind)
    max_row_len = max([el[1] for el in min_max_ind_list]) + 1
    print(max_row_len)

    for j, row in enumerate(area):
        area[j] += [' ']*(max_row_len - len(row))

    dirs = {'>': 0, 'v': 1, '<': 2, '^': 3}
    cur_dir = '>'
    coords = [0, area[0].index('.')]
    for instr in path:
        if isinstance(instr, int):
            for i in range(instr):
                area[coords[0]][coords[1]] = cur_dir
                if cur_dir == '>':
                    n_c = [coords[0], coords[1] + 1]
                    if n_c[1] > min_max_ind_list[n_c[0]][1]: n_c[1] = min_max_ind_list[n_c[0]][0]
                elif cur_dir == '<':
                    n_c = [coords[0], coords[1] - 1]
                    if n_c[1] < min_max_ind_list[n_c[0]][0]: n_c[1] = min_max_ind_list[n_c[0]][1]
                elif cur_dir == '^':
                    n_c = [coords[0] - 1, coords[1]]
                    if n_c[0] == -1:
                        n_c[0] += 1
                        while n_c[0] != max_ind + 1 and area[n_c[0]][n_c[1]] != ' ': n_c[0] += 1
                        n_c[0] -= 1
                    elif area[n_c[0]][n_c[1]] == ' ':
                        n_c[0] += 1
                        while n_c[0] != max_ind + 1 and area[n_c[0]][n_c[1]] != ' ':
                            n_c[0] += 1
                        n_c[0] -= 1
                elif cur_dir == 'v':
                    n_c = [coords[0] + 1, coords[1]]
                    if n_c[0] == max_ind + 1:
                        n_c[0] -= 1
                        while n_c[0] != -1 and area[n_c[0]][n_c[1]] != ' ': n_c[0] -= 1
                        n_c[0] += 1
                    elif area[n_c[0]][n_c[1]] == ' ':
                        n_c[0] -= 1
                        while n_c[0] != -1 and area[n_c[0]][n_c[1]] != ' ': n_c[0] -= 1
                        n_c[0] += 1
                else: n_c = [coords[0], coords[1]]

                if area[n_c[0]][n_c[1]] != '#':
                    coords = [n_c[0], n_c[1]]

        else:
            dir_l = list(dirs.keys())
            ind = dir_l.index(cur_dir)
            if instr == 'R': ind += 1
            else: ind -= 1
            cur_dir = dir_l[ind % len(dir_l)]

    area[coords[0]][coords[1]] = cur_dir
    coords = [coords[0] + 1, coords[1] + 1]

    for row in area:
        print(row)

    print(coords)
    print(1000*coords[0] + 4*coords[1] + dirs[cur_dir])

