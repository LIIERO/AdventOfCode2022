
from copy import deepcopy

class Rock:
    def __init__(self, shape, start_pos):
        self.shape = shape
        self.len = len(shape)
        self.pos = start_pos
        self.has_fallen = False

    def update_wind(self, wind, tower):
        is_movable = True
        for i, layer in enumerate(self.shape):
            ind, check = (layer[0] - 1, layer[0] > 0) if wind == '<' else (layer[-1] + 1, layer[-1] < 6)
            if not check:
                is_movable = False
                break
            elif tower[ind][self.pos + i] == '#':
                is_movable = False
                break

        if is_movable:
            for i, layer in enumerate(self.shape):
                for j, piece in enumerate(layer):
                    if wind == '<': self.shape[i][j] -= 1
                    if wind == '>': self.shape[i][j] += 1


def check_if_fallen_and_update(rock: Rock, tower, m_h):
    fallen = False
    for i, layer in enumerate(rock.shape):
        for point in layer:
            layer_pos = rock.pos + i
            if rock.pos == 0 or tower[point][layer_pos - 1] == '#':
                fallen = True
                break

    if fallen:
        for i, layer in enumerate(rock.shape):
            for point in layer:
                tower[point][rock.pos + i] = '#'
        new_m_h = rock.pos + rock.len
        if new_m_h > m_h: m_h = new_m_h

    return fallen, m_h

def main():
    """shapes = [
        ['..@@@@.'],
        ['...@...', '..@@@..', '...@...'],
        ['....@..', '....@..', '..@@@..'],
        ['..@....', '..@....', '..@....', '..@....'],
        ['..@@...', '..@@...']]"""

    shapes_num = [
        [[2, 3, 4, 5]],
        [[3], [2, 3, 4], [3]],
        [[2, 3, 4], [4], [4]],
        [[2], [2], [2], [2]],
        [[2, 3], [2, 3]]
    ]

    wind_data = txt_into_str()
    data_len = len(wind_data) - 1
    i_wind = 0
    max_height = 0
    # tower_height = [0]*7
    rang = 2022 # 2022
    t_range = rang * 4
    tower = [['.'] * t_range for _ in range(7)]
    for spawn in range(rang):
        rock = Rock(deepcopy(shapes_num[spawn%5]), max_height + 4)
        while not rock.has_fallen:
            rock.pos -= 1
            rock.update_wind(wind_data[i_wind], tower)


            fallen, max_height = check_if_fallen_and_update(rock, tower, max_height)
            if fallen: rock.has_fallen = True
            '''else:
                fallen, max_height = check_if_fallen_and_update(rock, tower, max_height)
                if fallen: rock.has_fallen = True'''

            # print(rock.has_fallen, max_height, wind_data[i_wind])
            i_wind = i_wind + 1 if i_wind != data_len else 0
        # print(np.array([row[::-1] for row in tower]).transpose())

    # print(np.array([row[::-1] for row in tower]).transpose())
    print(max_height)

