import ipfshttpclient
from src.Insert import Insert
from src.Search import Search
from src.parameters import *

node_1 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_1)
node_2 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_2)

res1 = node_1.add('test.txt')
res2 = node_2.add('test.txt')

print(res1)
print(res2)

print(node_1.id())
print(node_2.id())

insert = Insert('123', 'ciao')

print(insert.get_keyword())
print(insert.get_hash_obj())

search = Search(1,1)
bit_id = search.create_binary_id(5, 4)
print(bit_id)
bitset = search.create_bitset(bit_id)
print(bitset)

print(node_1.dht.findpeer(node_2.id()['ID'])) #cerca nella DHT il nodo con ID passato
print(node_1.dht.findprovs(res2['Hash'])) #cerca nella DHT i nodi che possono fornire l'oggetto il cui hash passato


node_1.close()
node_2.close()





