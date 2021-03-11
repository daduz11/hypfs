from src.utils import *

class Logic_node:
    def __init__(self, id):
        self.id = id #binario
        self.keywords = create_bitset(id)
        self.cids = []

    def get_id(self):
        return self.id

    def get_keywords(self):
        return self.keywords

    def get_cids(self):
        return self.cids

    def add_cid(self, cid):
        self.cids.append(cid)

