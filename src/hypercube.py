import networkx as nx
import matplotlib.pyplot as plt

from src.config import HYPERCUBE_SIZE
from src.utils import create_binary_id, NODES

LABELS = {tuple(int(j) for j in create_binary_id(i)): create_binary_id(i) for i in range(0, NODES)}


class Hypercube:
    def __init__(self):
        self.graph = nx.relabel_nodes(nx.generators.lattice.hypercube_graph(HYPERCUBE_SIZE), LABELS)

    def get_shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target)

    def plot_graph(self):
        nx.draw(self.graph, with_labels=True, font_weight='bold')
        plt.show()

    def depth_first_search(self, keyword=None, depth_limit=None):
        return [v for u, v, d in self.get_edges_dfs(keyword=keyword, depth_limit=depth_limit) if d == "forward"]

    def get_edges_dfs(self, keyword=None, depth_limit=None):
        # Based on http://www.ics.uci.edu/~eppstein/PADS/DFS.py
        # by D. Eppstein, July 2004.
        if keyword is None:
            # edges for all components
            nodes = self.graph
        else:
            # edges for components with source
            nodes = [keyword]
        visited = set()
        if depth_limit is None:
            depth_limit = len(self.graph)
        for start in nodes:
            if start in visited:
                continue
            yield start, start, "forward"
            visited.add(start)
            stack = [(start, depth_limit, iter(self.graph[start]))]
            while stack:
                parent, depth_now, children = stack[-1]
                try:
                    child = next(children)
                    if child in visited or parent > child:
                        yield parent, child, "non_tree"
                    else:
                        yield parent, child, "forward"
                        visited.add(child)
                        if depth_now > 1:
                            stack.append((child, depth_now - 1, iter(self.graph[child])))
                except StopIteration:
                    stack.pop()
                    if stack:
                        yield stack[-1][0], parent, "reverse"
            yield start, start, "reverse"
