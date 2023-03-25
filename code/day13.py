
def parse_array(str_arr: str):
    el = str_arr[1:-1]
    clean_el = []
    str_num = ''
    to_arr_slice_flag = False
    arr_slice = ''
    open_bracket_num = 0
    for i, char in enumerate(el):
        if char == '[' and not to_arr_slice_flag:
            to_arr_slice_flag = True
            open_bracket_num = 1
            arr_slice = '['
        elif to_arr_slice_flag:
            arr_slice += char
            if char == '[': open_bracket_num += 1
            elif char == ']': open_bracket_num -= 1
            if open_bracket_num == 0:
                to_arr_slice_flag = False
                clean_el.append(parse_array(arr_slice)) # recursion
        elif not to_arr_slice_flag:
            if char == ',' and str_num != '':
                clean_el.append(int(str_num))
                str_num = ''
            elif char != ',':
                str_num += char
                if i == len(el) - 1:
                    clean_el.append(int(str_num))
                    str_num = ''
    return clean_el


def compare_pair(left, right): # True jeśli prawa większa
    are_diff_len = True if len(left) != len(right) else False
    i = 0
    while True:
        if are_diff_len:
            try: r = right[i]
            except IndexError: return False
            try: l = left[i]
            except IndexError: return True
        else:
            if len(left) == 0: return None
            r = right[i]
            l = left[i]

        if isinstance(l, int) and isinstance(r, int):
            if r > l: return True
            if l > r: return False
        else:
            if isinstance(l, int): l = [l]
            if isinstance(r, int): r = [r]

        if isinstance(l, list) and isinstance(r, list):
            outcome = compare_pair(l, r)
            if outcome is not None:
                return outcome

        i += 1
        if i == len(left) and not are_diff_len:
            return None

def main(): # part 1
    data = txt_into_array()
    clean_data = []
    for el in data:
        if el != '': clean_data.append(parse_array(el))

    data_left = clean_data[::2]
    data_right = clean_data[1::2]

    sum_of_indices = 0
    for i, el_left in enumerate(data_left):
        if compare_pair(el_left, data_right[i]):
            sum_of_indices += i + 1

    print(sum_of_indices)



def quicksort(array): # part 2
    if len(array) < 2:
        return array  # Przypadek podstawowy
    else:
        pivot = array[0]  # Dowolny punkt (pierwszy dla wygody)
        less_than_pivot = [elem for elem in array[1:] if compare_pair(elem, pivot)]
        more_than_pivot = [elem for elem in array[1:] if compare_pair(pivot, elem)]

        return quicksort(less_than_pivot) + [pivot] + quicksort(more_than_pivot)  # Rekurencja

def main(): # part 2
    data = txt_into_array()
    clean_data = []
    for el in data:
        if el != '': clean_data.append(parse_array(el))
    clean_data = [[[2]], [[6]]] + clean_data

    sorted_data = quicksort(clean_data)

    for elem in sorted_data:
        print(elem)

    print((sorted_data.index([[2]]) + 1) * (sorted_data.index([[6]]) + 1))

