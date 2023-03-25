
def evaluate(field, x, y, cur, steps, visited):
    global solutions
    current = field[cur[1]][cur[0]]
    h = height[current]
    candidate = field[y][x]
    if (x, y) not in visited and height[candidate] in range(h, h + 2):
        if candidate == 'E':
            solutions.append(steps + 1)
        else:
            search(field, x, y, steps + 1, visited + (cur,))

def search(field, x, y, steps=0, visited=()):
    if x < len(field[0]) - 1:
        evaluate(field, x + 1, y, (x, y), steps, visited)
    if x > 0:
        evaluate(field, x - 1, y, (x, y), steps, visited)
    if y < len(field) - 1:
        evaluate(field, x, y + 1, (x, y), steps, visited)
    if y > 0:
        evaluate(field, x, y - 1, (x, y), steps, visited)


def main():

    print(height)
    data = [list(el) for el in txt_into_array('test_input')]
    for row in data:
        print(row)

    search(data, 0, 0)

    print(min(solutions))


if __name__ == '__main__':
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    height = {ch: i for i, ch in enumerate(char)}
    height['S'], height['E'] = 0, 25
    solutions = []
    main()

# ACTUAL CORRECT SOLUTION (DIJKSTRA UNUSED BUT COULD BE) =================================================

from collections import defaultdict
import heapq as heap

def dijkstra(G, startingNode):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingNode] = 0
    heap.heappush(pq, (0, startingNode))

    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        for adjNode in G[node]:
            if adjNode in visited:    continue

            newCost = nodeCosts[node] + 1
            if nodeCosts[adjNode] > newCost:
                parentsMap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))

    return parentsMap, nodeCosts


def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if not part_2:
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        print("Shortest path length = ", len(new_path) - 1)
                        return
                else:
                    if data[neighbour[1]][neighbour[0]] == 'a':
                        print("Shortest path from top to a = ", *new_path)
                        print("Shortest path from top to a length = ", len(new_path) - 1)
                        return

            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting path doesn't exist :(")
    return


def main():
    graph = {}
    final_node_coords, first_node_coords = (0, 0), (0, 0)
    for y, row in enumerate(data):
        for x, el in enumerate(row):
            cur = data[y][x]
            if cur == 'E': final_node_coords = (x, y)
            if cur == 'S': first_node_coords = (x, y)
            h = height[cur]
            rang = range(h + 2) if not part_2 else range(h - 1, h + 5)
            graph[(x, y)] = []
            if x < len(data[0]) - 1 and height[data[y][x + 1]] in rang:
                graph[(x, y)].append((x + 1, y))
            if x > 0 and height[data[y][x - 1]] in rang:
                graph[(x, y)].append((x - 1, y))
            if y < len(data) - 1 and height[data[y + 1][x]] in rang:
                graph[(x, y)].append((x, y + 1))
            if y > 0 and height[data[y - 1][x]] in rang:
                graph[(x, y)].append((x, y - 1))

    print(final_node_coords)
    if part_2: first_node_coords, final_node_coords = final_node_coords, first_node_coords
    BFS_SP(graph, first_node_coords, final_node_coords)

    # parentsMap, nodeCosts = dijkstra(graph, (0, 0))
    # print(nodeCosts[final_node_coords])

if __name__ == '__main__':
    part_2 = True

    data = [list(el) for el in txt_into_array()]
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    height = {ch: i for i, ch in enumerate(char)}
    height['S'], height['E'] = 0, 25

    main()

