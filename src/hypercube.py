from src.utils import *
import networkx as nx
import matplotlib.pyplot as plt


LABELS = {tuple(int(j) for j in create_binary_id(i)): create_binary_id(i) for i in range(0, NODES)}


class Hypercube:
    def __init__(self):
        self.graph = nx.relabel_nodes(nx.generators.lattice.hypercube_graph(HYPERCUBE_SIZE), LABELS)

    def get_shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target)

    def plot_graph(self):
        nx.draw(self.graph, with_labels=True, font_weight='bold')
        plt.show()

    def breadth_first_search(self, keyword=None):
        levels = self.breadth_first_levels(keyword)
        nodes = []
        for i in levels:
            for j in i:
                nodes.append(j)
        return nodes

    def breadth_first_levels(self, root):
        # Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
        # by D. Eppstein, July 2004.
        visited = set()
        current_level = [root]
        while current_level:
            for v in current_level:
                visited.add(v)
            next_level = set()
            level_graph = {v: set() for v in sorted(current_level, reverse=True)}
            for v in current_level:
                for w in self.graph[v]:
                    if w not in visited and w > v:
                        level_graph[v].add(w)
                        next_level.add(w)
            yield level_graph
            current_level = next_level
