from flask import Response

from src.hypercube import Hypercube
from src.parameters import *
from src.utils import *


class Node:
    def __init__(self, int_id):
        self.id = create_binary_id(int_id)
        self.hypercube = Hypercube()
        self.objects = []

    def get_id(self):
        return self.id

    def get_objects(self):
        return self.objects

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)

    def insert(self, keyword, object):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            if not object in self.objects:
                self.objects.append(object)
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            next_node = best_path[1]
            request(next_node, INSERT, keyword, object)

    def remove(self, keyword, object):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            if object in self.objects:
                self.objects.remove(object)
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            neighbor = best_path[1]
            request(neighbor, REMOVE, keyword, object)

    def pin_search(self, keyword):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            return self.objects
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            neighbor = best_path[1]
            return request(neighbor, PIN_SEARCH, keyword, object)





