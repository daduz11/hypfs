import ipfshttpclient
from src.insert import Insert
from src.logic_node import Logic_node
from src.physical_node import Physical_node
from src.search import Search
from src.parameters import *
from src.network import Network
from src.hypercube import Hypercube

node_1 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_1)
node_2 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_2)

res1 = node_1.add('test.txt')
res2 = node_2.add('test.txt')

print(res1)
print(res2)

print(node_1.id())
print(node_2.id())

#print(node_1.dht.findpeer(node_2.id()['ID'])) #cerca nella DHT il nodo con ID passato
#print(node_1.dht.findprovs(res2['Hash'])) #cerca nella DHT i nodi che possono fornire l'oggetto il cui hash passato

network = Network()
for i in range(0, 2):
    node = Physical_node(i)
    if not network.add_node(node):
        print('Error: node {} not added'.format(i))


network.get_node(0).hypercube.insert(1, res2['Hash'])
network.get_node(0).hypercube.insert(1, res1['Hash'])
print(network.get_node(0).hypercube.get_logic_node(1).get_cids())
node_1.close()
node_2.close()





