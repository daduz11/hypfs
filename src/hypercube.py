from src.utils import *
import networkx as nx
import matplotlib.pyplot as plt


class Hypercube:
    def __init__(self):
        self.graph = nx.Graph()
        for i in range(0, LOGIC_NODES):
            self.graph.add_node(create_binary_id(i))
        for i in range(0, LOGIC_NODES):
            for j in range(0, LOGIC_NODES):
                if hamming_distance(i, j) == 1:
                    self.graph.add_edge(create_binary_id(i), create_binary_id(j))

    def get_shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target)

    def pin_search(self, keyword):
        bit_id = create_binary_id(keyword)
        if bit_id in self.nodes:
            return self.nodes[bit_id].get_objects()
        else:
            return None

    def superset_search(self, keyword, depth_limit=HYPERCUBE_SIZE):
        objects = []
        superset = list(self.depth_first_search(keyword=create_binary_id(keyword), depth_limit=depth_limit))
        print(superset)
        for id in superset:
            if id in self.nodes:
                objects.extend(self.nodes[id].get_objects())
            else:
                continue
        return objects

    def remove(self, cid):
        found = False
        for logic_node in self.nodes.keys():
            for icid in self.nodes[logic_node].get_objects():
                if icid == cid:
                    self.nodes[logic_node].remove_object(cid)
                    return True
        if not found:
            return False

    def get_logic_node(self, id):
        return self.nodes[create_binary_id(id)]

    def plot_graph(self):
        nx.draw(self.graph, with_labels=True, font_weight='bold')
        plt.show()

    def depth_first_search(self, keyword=None, depth_limit=None):
        edges = self.do_search(keyword=keyword, depth_limit=depth_limit)
        return (v for u, v, d in edges if d == "forward")

    def do_search(self, keyword=None, depth_limit=None):
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
                    if child in visited or int(keyword, 2) > int(child, 2):
                        yield parent, child, "nontree"
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
