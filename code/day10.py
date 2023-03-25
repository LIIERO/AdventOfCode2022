
def main():
    data = [[val if i == 0 else int(val) for i, val in enumerate(el.split())] for el in txt_into_array()]
    cycles_len = {'addx': 2, 'noop': 1}

    CRT = [[' ']*40 for _ in range(6)]

    X = 1
    cur_cycle = 0
    for instr in data:
        ins = instr[0]
        for rnd in range(cycles_len[ins]):
            cur_cycle += 1


            pos_to_draw = cur_cycle - 1
            y_pos = pos_to_draw//40
            pos_to_draw = pos_to_draw % 40
            CRT[y_pos][pos_to_draw] = '#' if pos_to_draw in range(X-1, X+2) else '.'

            if ins == 'addx' and rnd == 1:
                X += instr[1]


    for row in CRT:
        print(row)

