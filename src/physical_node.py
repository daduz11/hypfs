from src.hypercube import Hypercube


class Physical_node:
    def __init__(self, id):
        self.id = id
        self.hypercube = Hypercube(id)
        self.neighbours = []

    def get_id(self):
        return self.id

