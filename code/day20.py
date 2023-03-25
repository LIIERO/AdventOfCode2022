
def main():
    mul = 811589153 # 811589153
    order = [int(el)*mul for el in txt_into_array()]
    d_len = len(order)
    data = [(i, el) for i, el in enumerate(order)]

    # data = [El(el, j) for j, el in enumerate(data)]
    # found_first = False
    rang = 10 # 10
    for _ in range(rang):
        n_swaps = 0
        while n_swaps < d_len:
            ind_from = data.index((n_swaps, order[n_swaps]))
            el = data.pop(ind_from)
            ind = (ind_from + el[1]) % (d_len - 1)
            data.insert(ind, el)
            n_swaps += 1
        # print(_, [el.val for el in data])


    data = [el[1] for el in data]
    print(data)
    i_good = 2137
    for i, num in enumerate(data):
        if num == 0:
            i_good = i
            break
    s = 0
    for k in [1000, 2000, 3000]:
        v = data[(k + i_good) % d_len]
        print(v)
        s += v

    print(s)

