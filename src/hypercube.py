from src.logic_node import Logic_node
from src.parameters import NETWORK_SIZE
from src.utils import *


class Hypercube:
    def __init__(self, physical_id):
        self.nodes = []
        self.capacity = HYPERCUBE_SIZE
        for i in range(int(physical_id * (2**self.capacity / NETWORK_SIZE)), int((physical_id + 1) * (2**self.capacity / NETWORK_SIZE))):
            self.nodes.append(Logic_node(create_binary_id(i)))

    def insert(self, keyword, cid):
        bit_id = create_binary_id(keyword)
        for logic_node in self.nodes:
            if bit_id == logic_node.get_id():
                logic_node.add_cid(cid)

    def pin_search(self, keyword):
        found = False
        bit_id = create_binary_id(keyword)
        for logic_node in self.nodes:
            if bit_id == logic_node.get_id():
                found = True
                return logic_node.get_cids()
        if not found:
            return None

    def superset_search(self, keyword):
        bit_nodes = get_binary_combination(keyword)
        results = []
        for bit_node in bit_nodes:
            found = False
            for logic_node in self.nodes:
                if logic_node.get_id() == bit_node:
                    results.extend(logic_node.get_cids())
                    found = True
            if not found:
                continue
        return list(set(results))

    def remove(self, cid):
        found = False
        for logic_node in self.nodes:
            for icid in logic_node.get_cids():
                if icid == cid:
                    logic_node.remove_cid(cid)
                    return True
        if not found:
            return False

    def get_logic_node(self, id):
        return self.nodes[id]

    def get_node_id_list(self):
        ids = []
        for node in self.nodes:
            ids.append(node.get_id())
        return ids
