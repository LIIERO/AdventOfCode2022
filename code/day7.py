
def value_sum(d):
    val_sum = 0
    for key, val in d.items():
        if key == 'f_val':
            val_sum += sum(val)
        else:
            val_sum += value_sum(d[key])
    return val_sum

def big_enough_dirs(d, miss):
    global good_dirs
    val_sum = value_sum(d)
    if val_sum >= miss: good_dirs.append(val_sum)
    for key, val in d.items():
        if key != 'f_val':
            big_enough_dirs(d[key], miss)

def main():
    data = txt_into_array()
    data = [el.split(' ') for el in data]
    # print(data)

    cur_dir = []
    data_clean = {}
    for el in data:
        if el[0] == '$' and el[1] == 'cd':
            dir_name = el[2]
            if dir_name == '..':
                cur_dir.pop()
            else:
                cur_dir.append(dir_name)
                nested_set(data_clean, cur_dir, {'f_val': []})

        elif el[0] not in ['$', 'dir']:
            nested_append(data_clean, cur_dir + ['f_val'], int(el[0]))

    unused_space = 70000000 - value_sum(data_clean)
    missing = 30000000 - unused_space
    big_enough_dirs(data_clean, missing)
    print(min(good_dirs))

if __name__ == '__main__':
    good_dirs = []
    main()

