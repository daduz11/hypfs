from client import Client, NODES, create_binary_id
from src.hypercube import Hypercube
from src.node import Node
from src.parameters import *

client_1 = Client(IPFS_CLIENT_ADDRESS_1, 0)
client_2 = Client(IPFS_CLIENT_ADDRESS_1, 1)



hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt', 1)
hash_1 = client_1.add_obj('test2.txt',2)
hash_1 = client_1.add_obj('test.txt',3)
hash_1 = client_1.add_obj('test2.txt',4)
hash_1 = client_1.add_obj('test.txt',5)
hash_1 = client_1.add_obj('test2.txt',6)
hash_1 = client_1.add_obj('test.txt',7)
hash_1 = client_1.add_obj('test2.txt',1)
hash_1 = client_1.add_obj('test.txt',2)
hash_1 = client_1.add_obj('test2.txt',3)
hash_1 = client_1.add_obj('test.txt',4)
hash_1 = client_1.add_obj('test2.txt',5)
hash_1 = client_1.add_obj('test.txt',6)
hash_1 = client_1.add_obj('test2.txt',7)
hash_1 = client_1.add_obj('test.txt',1)
#hash_1 = client_1.add_obj('test2.txt')
#hash_1 = client_1.add_obj('test.txt')
#client_1.remove_obj('QmXb9edthGYiMDRpr3y82u1daYgpdmewitArf1wTU46mCs', 2)
#client_1.pin_search(3)
client_1.superset_search(1)

client_1.get_obj(input())

print()

client_1.close()
