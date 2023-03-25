
def main():
    data = txt_into_array()

    # op = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    strat_dict = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

    rew = {'A': 1, 'B': 2, 'C': 3}
    win = {'A': 'B', 'B': 'C', 'C': 'A'}
    loss = {'A': 'C', 'B': 'A', 'C': 'B'}

    data = [[el[0], el[-1]] for el in data]
    # print(data)

    points_sum = 0
    for gr in data:
        points = 0
        enemy, strat = gr[0], strat_dict[gr[1]]
        if strat == 'lose': you = loss[enemy]
        elif strat == 'win': you = win[enemy]
        else: you = enemy

        points += rew[you]
        if enemy == you: points += 3
        elif win[enemy] == you: points += 6

        points_sum += points

    print(points_sum)

