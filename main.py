import ipfshttpclient

from client import Client
from src.parameters import *

client_2 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_2)


client_1 = Client(IPFS_CLIENT_ADDRESS_1, 0)
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
#print(node_1.dht.findpeer(node_2.id()['ID'])) #cerca nella DHT il nodo con ID passato
#print(node_1.dht.findprovs(res2['Hash'])) #cerca nella DHT i nodi che possono fornire l'oggetto il cui hash passato

#print(list(node_1.swarm.addrs()['Addrs']))


#node_1.dht.query(node_2.id()['ID'])
#node_2.dht.query(node_1.id()['ID'])



"""
try:
    node_1.swarm.connect(IPFS_CLIENT_ADDRESS_2 + '/ipfs/' + node_2.id()['ID'])
except Exception:
    pass
print(list(node_1.swarm.addrs()['Addrs']))


print(list(node_2.swarm.addrs()['Addrs']))
"""
client_1.close()
client_2.close()





