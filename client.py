from random import randint
import ipfshttpclient
from src.utils import *


class Client:
    def __init__(self, addr, server):
        self.ipfs = ipfshttpclient.connect(addr)
        self.id = self.ipfs.id()['ID']
        self.server = server
        log(self.id, 'CONNECTION', '{}'.format(addr))

    def add_obj(self, path, keyword=randint(0, NODES-1)):
        obj_hash = self.ipfs.add(path)['Hash']
        if request(create_binary_id(self.server), INSERT, {'keyword': str(keyword), 'obj': obj_hash}).text == 'success':
            log(self.id, INSERT, 'REFERENCE ({},{}) ADDED'.format(keyword, obj_hash))
        else:
            log(self.id, INSERT, 'REFERENCE ({},{}) ALREADY EXIST'.format(keyword, obj_hash))
        return

    def remove_obj(self, obj_hash, keyword=randint(0, NODES-1)):
        if request(create_binary_id(self.server), REMOVE, {'keyword': str(keyword), 'obj': obj_hash}).text == 'success':
            log(self.id, REMOVE, 'REFERENCE ({},{}) REMOVED'.format(keyword, obj_hash))
        else:
            log(self.id, REMOVE, 'REFERENCE ({},{}) NOT EXIST'.format(keyword, obj_hash))
        return

    def get_obj(self, obj):
        try:
            self.ipfs.get(obj, target='./objects')
            log(self.id, 'GET', "OBJECT '{}' DOWNLOADED".format(obj))
        except Exception:
            log(self.id, 'GET', "OBJECT '{}' NOT FOUND".format(obj))

    def pin_search(self, keyword=randint(0, NODES-1), threshold=-1):
        if threshold == -1:
            res = request(create_binary_id(self.server), PIN_SEARCH, {'keyword': str(keyword)}).text.split(',')
        else:
            res = request(create_binary_id(self.server), PIN_SEARCH, {'keyword': str(keyword), 'threshold': threshold}).text.split(',')
        if len(res) > 0:
            log(self.id, PIN_SEARCH, '{}'.format(res))
        else:
            log(self.id, PIN_SEARCH, 'NO RESULTS FOUND')
        return

    def superset_search(self, keyword=randint(0, NODES-1), threshold=SUPERSET_THRESHOLD):
        res = request(create_binary_id(self.server), SUPERSET_SEARCH, {'keyword': str(keyword), 'threshold': threshold}).text.split(',')
        if len(res) > 0:
            log(self.id, SUPERSET_SEARCH, '{}'.format(res))
        else:
            log(self.id, SUPERSET_SEARCH, 'NO RESULTS FOUND')
        return

    def close(self):
        self.ipfs.close()
        return
