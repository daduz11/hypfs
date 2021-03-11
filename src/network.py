from src.parameters import NETWORK_SIZE


class Network:
    def __init__(self):
        self.nodes = []
        self.capacity = NETWORK_SIZE

    def add_node(self, node):
        if len(self.nodes) < self.capacity:
            self.nodes.append(node)
            return True
        else:
            return False

    def get_node(self, index):
        if index in range(0, len(self.nodes)):
            return self.nodes[index]
        else:
            return None

    def remove_node(self, index=-1):
        if len(self.nodes) > 0 and index in range(-1, len(self.nodes)):
            self.nodes.pop(index)
            return True
        else:
            return False

    def reset_network(self):
        self.nodes = []
        self.capacity = NETWORK_SIZE

    def set_capacity(self, capacity):
        if capacity > 0:
            self.capacity = capacity
            return self.capacity
        else:
            return False

    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return len(self.nodes)

