from client import Client
from src.parameters import *


client_1 = Client(IPFS_CLIENT_ADDRESS_1, 0)
client_2 = Client(IPFS_CLIENT_ADDRESS_1, 1)

hash_1 = client_1.add_obj('test.txt', 3)
hash_1 = client_1.add_obj('test2.txt')
hash_1 = client_1.add_obj('test.txt')
hash_1 = client_1.add_obj('test2.txt')
hash_1 = client_1.add_obj('test.txt')
client_1.remove_obj('QmXb9edthGYiMDRpr3y82u1daYgpdmewitArf1wTU46mCs', 2)
client_1.pin_search(3)
client_1.superset_search(2)

client_1.get_obj(input())

print()

client_1.close()





