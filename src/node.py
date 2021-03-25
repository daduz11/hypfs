from src.config import SEARCH_TYPE, HOP_SERVER_PORT
from src.hypercube import Hypercube
from src.utils import *
import threading


class Node:
    def __init__(self, int_id):
        self.id = create_binary_id(int_id)
        self.hypercube = Hypercube()
        self.objects = []
        self.lock = threading.Lock()

    def insert(self, keyword, obj):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            if obj not in self.objects:
                with self.lock:
                    self.objects.append(obj)
                    return 'success'
            else:
                return 'failure'
        else:
            neighbor = self.hypercube.get_shortest_path(self.id, bit_keyword)[1]
            return request(neighbor, INSERT, {'keyword': str(keyword), 'obj': obj})

    def remove(self, keyword, obj):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            if obj in self.objects:
                with self.lock:
                    self.objects.remove(obj)
                    return 'success'
            else:
                return 'failure'
        else:
            neighbor = self.hypercube.get_shortest_path(self.id, bit_keyword)[1]
            return request(neighbor, REMOVE, {'keyword': str(keyword), 'obj': obj})

    def pin_search(self, keyword, threshold=-1):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            return self.get_objects(threshold)
        else:
            neighbor = self.hypercube.get_shortest_path(self.id, bit_keyword)[1]
            return request(neighbor, PIN_SEARCH, {'keyword': str(keyword), 'threshold': threshold})

    def superset_search(self, keyword, threshold, sender):
        bit_keyword = create_binary_id(keyword)
        if one(bit_keyword) != one(self.id) and sender == 'user':
            neighbor = self.hypercube.get_shortest_path(self.id, bit_keyword)[1]
            return request(neighbor, SUPERSET_SEARCH, {'keyword': keyword, 'threshold': threshold, 'sender': 'user'})
        else:
            results = []
            objects = self.get_objects(threshold)
            results.extend(objects)
            threshold -= len(objects)
            for neighbor in self.get_neighbors(bit_keyword):
                if threshold <= 0:
                    break
                else:
                    result = get_response(request(neighbor, SUPERSET_SEARCH, {'keyword': keyword, 'threshold': threshold, 'sender': 'node'}).text)
                    results.extend(result)
                    threshold -= len(result)
            return results

    def get_neighbors(self, keyword):
        if SEARCH_TYPE == 'BFS':
            tree = self.hypercube.breadth_first_search(keyword)
        else:
            tree = self.hypercube.depth_first_search(keyword)
        return [tree[i] for i in range(tree.index(self.id), len(tree)) if hamming_distance(get_decimal(tree[i]), get_decimal(self.id)) == 1 and self.id < tree[i]]

    def get_objects(self, threshold):
        with self.lock:
            if 0 < threshold < len(self.objects):
                return self.objects[:threshold]
            else:
                return self.objects
