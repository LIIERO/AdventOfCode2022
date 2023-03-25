
def main():
    count = 0
    for pair in [[[int(val) for val in ran.split('-')] for ran in el.split(',')] for el in txt_into_array()]:
        if pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1]: count += 1
    print(count)

