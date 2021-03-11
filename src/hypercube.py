from src.logic_node import Logic_node
from src.parameters import NETWORK_SIZE
from src.utils import *

class Hypercube:
    def __init__(self, physical_id):
        self.nodes = []
        self.capacity = HYPERCUBE_SIZE
        for i in range(int(physical_id * (2**self.capacity / NETWORK_SIZE)), int((physical_id + 1) * (2**self.capacity / NETWORK_SIZE))):
            bit_id = create_binary_id(i)
            self.nodes.append(Logic_node(bit_id))

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

    def get_logic_node(self, id):
        return self.nodes[id]
