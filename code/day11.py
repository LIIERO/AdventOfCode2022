
from copy import copy

class Monkey:
    WORRY_DIV = 3
    MODULUS = 1
    def __init__(self, monkey_id: int, start_items: list, operation: tuple, div_by: int, which_monkey: dict):
        self.items = start_items # Zmieniają się
        self.no_inspected = 0

        self.id = monkey_id # Nie zmieniają się
        self.op_sign = operation[0]
        self.op_val = operation[1]
        self.div_by = div_by
        self.choice = copy(which_monkey)

    def take_turn(self):
        giveaway = {self.choice[True]: [], self.choice[False]: []}
        for item in self.items:
            op_by = item if self.op_val == 'old' else int(self.op_val)
            item = item * op_by if self.op_sign == '*' else item + op_by
            # item = item//Monkey.WORRY_DIV
            item = item % Monkey.MODULUS
            giveaway[self.choice[item % self.div_by == 0]].append(item)
            self.no_inspected += 1
        self.items = []
        # print(self.id, giveaway)
        return giveaway


def main():
    data = txt_into_array()
    monkey_list = []
    no_monkey, start_items, op, div_by, which_monkey = 0, [], (), 0, {True: 0, False: 0}
    for line in data:
        if line[:3] == 'Sta': start_items = [int(el[:-1]) if el[-1] == ',' else int(el) for el in line.split(' ')[2:]]
        if line[:3] == 'Ope': op = tuple(line.split(' ')[-2:])
        if line[:3] == 'Tes':
            div_by = int(line.split(' ')[-1])
            Monkey.MODULUS *= div_by
        if line[:4] == 'If t': which_monkey[True] = int(line.split(' ')[-1])
        if line[:4] == 'If f': which_monkey[False] = int(line.split(' ')[-1])
        if line == '':
            monkey_list.append(Monkey(no_monkey, start_items, op, div_by, which_monkey))
            no_monkey += 1
    monkey_list.append(Monkey(no_monkey, start_items, op, div_by, which_monkey))

    for rnd in range(10000):
        #print(rnd, [m.items for m in monkey_list])
        for monkey in monkey_list:
            give = monkey.take_turn()
            for no_monkey, item_list in give.items():
                monkey_list[no_monkey].items += item_list

    val_list = []
    for monkey in monkey_list:
        print(monkey.id, monkey.no_inspected)
        val_list.append(monkey.no_inspected)

    val_list.sort(reverse=True)
    print(val_list[0] * val_list[1])

