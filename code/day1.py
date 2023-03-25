
def main():
    data = txt_into_int_array()

    added_lst = []
    s = 0
    for line in data:
        if line:
            s += line
        else:
            added_lst.append(s)
            s = 0
    added_lst.sort(reverse=True)
    added_lst = added_lst[:3]
    print(sum(added_lst))


