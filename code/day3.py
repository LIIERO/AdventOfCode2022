
def main():
    data = txt_into_array('test_input')
    data = [[el[:len(el)//2], el[len(el)//2:]] for el in data]

    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    el_sum = 0
    for rucksack in data:
        for el in rucksack[0]:
            if el in rucksack[1]:
                val = 1
                if el.isupper():
                    val += 26
                    el = el.lower()
                val += char.index(el)
                el_sum += val
                break
    print(el_sum)

def main():
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    data = txt_into_array()
    # new_data = []
    val_sum = 0
    counter = 0
    group = []
    for rucksack in data:
        group.append(rucksack)
        counter += 1
        if counter == 3:
            counter = 0
            # new_data.append(group)

            for el in group[0]:
                if el in group[1] and el in group[2]:
                    val = 1
                    if el.isupper():
                        val += 26
                        el = el.lower()
                    val += char.index(el)
                    val_sum += val
                    break

            group = []

    print(val_sum)

