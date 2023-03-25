
def main():
    data = txt_into_array()
    data = [[int(el) for el in row] for row in data]
    X, Y = len(data), len(data[0])

    highest_score = 0
    for i in range(X):
        for j in range(Y):
            score = calculate_score(data, i, j, X, Y)
            if score > highest_score:
                highest_score = score
    print(highest_score)

def calculate_score(mat, x, y, X, Y):
    score = 1
    el = mat[x][y]

    ind_score = [0, 0, 0, 0]

    for k in reversed(range(y)): # left
        ind_score[0] += 1
        if mat[x][k] >= el: break
    for k in range(y + 1, Y):  # right
        ind_score[1] += 1
        if mat[x][k] >= el: break
    for k in reversed(range(x)):  # up
        ind_score[2] += 1
        if mat[k][y] >= el: break
    for k in range(x + 1, X):  # down
        ind_score[3] += 1
        if mat[k][y] >= el: break

    for i_s in ind_score:
        score *= i_s

    return score

