
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():
    y_to_check = 10

    data = txt_into_array()
    data = [[val[2:] for i, val in enumerate(el.split(' ')) if i in [2, 3, 8, 9]] for el in data]
    data = [[int(el[:-1]) if el[-1] in [':', ','] else int(el) for el in line] for line in data]
    data = {tuple(line[:2]): tuple(line[2:]) for line in data}
    min_x, min_y, max_x, max_y = inf, inf, 0, 0
    max_distance = 0
    for sensor, beacon in data.items():
        if sensor[0] < min_x: min_x = sensor[0]
        if beacon[0] < min_x: min_x = beacon[0]
        if sensor[1] < min_y: min_y = sensor[1]
        if beacon[1] < min_y: min_y = beacon[1]
        if sensor[0] > max_x: max_x = sensor[0]
        if beacon[0] > max_x: max_x = beacon[0]
        if sensor[1] > max_y: max_y = sensor[1]
        if beacon[1] > max_y: max_y = beacon[1]
        d = distance(sensor, beacon)
        if d > max_distance: max_distance = d
    print(data)
    print(min_x, min_y, max_x, max_y)
    print(max_distance)
    scale_x, scale_y = max_distance - min_x, max_distance - min_y
    print(scale_x, scale_y)
    size_x, size_y = (max_x - min_x) + 1 + 2*max_distance, (max_y - min_y) + 1 + 2*max_distance
    print(size_x, size_y)

    area_ytc = ['.']*size_x

    for sensor, beacon in data.items():
        if beacon[1] == y_to_check:
            area_ytc[beacon[0] + scale_x] = 'B'
            continue

        dist = distance(sensor, beacon)
        diff = abs(y_to_check - sensor[1])
        if dist >= diff:
            steps = dist - diff
            for i in range(sensor[0] - steps, sensor[0] + steps + 1):
                if area_ytc[i + scale_x] not in ['B', '#']: area_ytc[i + scale_x] = '#'

    no_hashes = 0
    for el in area_ytc:
        if el == '#': no_hashes += 1

    print(no_hashes)

