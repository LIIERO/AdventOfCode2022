
def main():
    data = [[val if i == 0 else int(val) for i, val in enumerate(el.split())] for el in txt_into_array('test_input')]
    H_pos, T_pos = [0, 0], [0, 0]
    print(data)
    already_visited = [(0, 0)]
    for instr in data:
        d = instr[0]
        for inst_it in range(instr[-1]):
            # Head movement
            if d == 'R': H_pos[0] += 1
            elif d == 'L': H_pos[0] -= 1
            elif d == 'U': H_pos[1] += 1
            elif d == 'D': H_pos[1] -= 1

            # Tail movement
            x_diff = H_pos[0] - T_pos[0]
            y_diff = H_pos[1] - T_pos[1]
            if abs(x_diff) <= 1 and abs(y_diff) <= 1: continue

            if x_diff > 0: T_pos[0] += 1
            elif x_diff < 0: T_pos[0] -= 1
            if y_diff > 0: T_pos[1] += 1
            elif y_diff < 0: T_pos[1] -= 1

            pos = tuple(T_pos)
            if pos not in already_visited:
                already_visited.append(pos)

    print(len(already_visited))

from funcs import *
# import numpy as np

class Node:
    TRAIL_LENGTH = 10
    last_node_pos = (0, 0)
    def __init__(self, i_d: int, parent=None):
        self.x: int = 0
        self.y: int = 0
        self.id: int = i_d
        self.parent = parent

        next_id = i_d + 1
        self.child = None if next_id == Node.TRAIL_LENGTH else Node(next_id, self)

    def update(self):
        if self.parent is not None:
            x_diff = self.parent.x - self.x
            y_diff = self.parent.y - self.y
            if abs(x_diff) > 1 or abs(y_diff) > 1:
                if x_diff > 0: self.x += 1
                elif x_diff < 0: self.x -= 1
                if y_diff > 0: self.y += 1
                elif y_diff < 0: self.y -= 1

        if self.child is not None: self.child.update()
        else: Node.last_node_pos = (self.x, self.y)


def main():
    data = [[val if i == 0 else int(val) for i, val in enumerate(el.split())] for el in txt_into_array()]

    head = Node(0)
    already_visited = [(0, 0)]
    for instr in data:
        d = instr[0]
        for inst_it in range(instr[-1]):
            if d == 'R': head.x += 1
            elif d == 'L': head.x -= 1
            elif d == 'U': head.y += 1
            elif d == 'D': head.y -= 1

            head.update()

            pos = Node.last_node_pos
            if pos not in already_visited:
                already_visited.append(pos)

    print(len(already_visited))

if __name__ == '__main__':
    main()

