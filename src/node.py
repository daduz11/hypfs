from src.hypercube import Hypercube
from src.utils import *
import threading

class Node:
    def __init__(self, int_id):
        self.id = create_binary_id(int_id)
        self.hypercube = Hypercube()
        self.objects = []
        self._lock = threading.Lock()

    def insert(self, keyword, obj):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            if obj not in self.objects:
                with self._lock:
                    self.objects.append(obj)
                    return 'success'
            else:
                return 'failure'
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            neighbor = best_path[1]
            return request(neighbor, INSERT, {'keyword': str(keyword), 'obj': obj})

    def remove(self, keyword, obj):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            if obj in self.objects:
                with self._lock:
                    self.objects.remove(obj)
                    return 'success'
            else:
                return 'failure'
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            neighbor = best_path[1]
            return request(neighbor, REMOVE, {'keyword': str(keyword), 'obj': obj})

    def pin_search(self, keyword, threshold=-1):
        bit_keyword = create_binary_id(keyword)
        if bit_keyword == self.id:
            with self._lock:
                if 0 < threshold < len(self.objects):
                    return self.objects[:threshold]
                else:
                    return self.objects
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            neighbor = best_path[1]
            return request(neighbor, PIN_SEARCH, {'keyword': str(keyword), 'threshold': threshold})

    def superset_search(self, keyword, threshold, superset=None):
        bit_keyword = create_binary_id(keyword)
        if superset is None:
            superset = ','.join(self.hypercube.breadth_first_search(bit_keyword))
        if self.id == bit_keyword:
            superset = list(superset.split(','))
            results = []
            for target in superset:
                if threshold <= 0:
                    break
                if self.id == target:
                    with self._lock:
                        if 0 < threshold < len(self.objects):
                            result = self.objects[:threshold]
                        else:
                            result = self.objects
                        results.extend(result)
                        threshold -= len(result)
                else:
                    best_path = self.hypercube.get_shortest_path(self.id, target)
                    neighbor = best_path[1]
                    result = list(request(neighbor, PIN_SEARCH, {'keyword': int(target, 2), 'threshold': threshold}).text.split(','))
                    threshold -= len(result)
                    results.extend(result)
            return results
        else:
            best_path = self.hypercube.get_shortest_path(self.id, bit_keyword)
            neighbor = best_path[1]
            return request(neighbor, SUPERSET_SEARCH, {'keyword': keyword, 'threshold': threshold, 'superset': superset})

