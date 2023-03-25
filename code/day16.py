
class Node:
    def __init__(self, label, flow_rate):
        self.label = label
        self.flow_rate = flow_rate

        self.opened = False
        self.press_generated = 0

    def get_pot_press(self, time):
        return (time - 1) * self.flow_rate

    def update_node(self):
        if self.opened:
            self.press_generated += self.flow_rate


def search(G, N, cur_node, time_left):
    if N[cur_node].flow_rate < 10:
        for n in G[cur_node]:
            search(G, N, n, time_left - 1)


def main():
    data = txt_into_array('test_input')
    flow_data = {line.split()[1]: int(line.split()[4].split('=')[-1][:-1]) for line in data}
    graph = {line.split()[1]: [el[:2] for el in line.split()[9:]] for line in data}
    N = {name: Node(name, flow_data[name]) for name in graph.keys()}
    search(graph, N, 'AA', 30)

