
def main():
    data = txt_into_array_raw('test_input')
    ind = data.index('')
    data_slice = [[el[i:i+4].strip(" []") for i in range(0, len(el), 4)] for i, el in enumerate(data) if i < ind - 1][::-1]
    data_stack = [[el for el in stack if el != ''] for stack in list(map(list, zip(*data_slice)))]
    data_instructions = [[int(val) for val in el.split(' ')[1::2]] for i, el in enumerate(data) if i > ind]

    for instr in data_instructions:
        for _ in range(instr[0]):
            el = data_stack[instr[1]-1].pop()
            data_stack[instr[2]-1].append(el)

    result = ''
    for stack in data_stack: result += stack[-1]
    print(result)

def main():
    data = txt_into_array_raw()
    ind = data.index('')
    data_slice = [[el[i:i+4].strip(" []") for i in range(0, len(el), 4)] for i, el in enumerate(data) if i < ind - 1][::-1]
    data_stack = [[el for el in stack if el != ''] for stack in list(map(list, zip(*data_slice)))]
    data_instructions = [[int(val) for val in el.split(' ')[1::2]] for i, el in enumerate(data) if i > ind]

    for instr in data_instructions:
        ind_from, ind_to = instr[1]-1, instr[2]-1
        el = data_stack[ind_from][-instr[0]:]
        del data_stack[ind_from][-instr[0]:]
        data_stack[ind_to] += el

    result = ''
    for stack in data_stack: result += stack[-1]
    print(result)

