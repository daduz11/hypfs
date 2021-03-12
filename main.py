import ipfshttpclient
from src.physical_node import Physical_node
from src.parameters import *
from src.network import Network


node_1 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_1)
node_2 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_2)

res1 = node_1.add('test.txt')
res2 = node_2.add('test2.txt')

print(res1)
print(res2)

print(node_1.id()) #12D3KooWDYSvSoJZn3HmJsK6fvVikeRKyGbqT7dueXZsGgLoLoJ5
print(node_2.id()) #12D3KooWJdRd7Gp6qLuzNrEJCgkP9MsvfQu7oqfgs6xYWKiS2wqV

#print(node_1.dht.findpeer(node_2.id()['ID'])) #cerca nella DHT il nodo con ID passato
#print(node_1.dht.findprovs(res2['Hash'])) #cerca nella DHT i nodi che possono fornire l'oggetto il cui hash passato

network = Network()
for i in range(0, NETWORK_SIZE):
    node = Physical_node(i)
    if not network.add_node(node):
        print('Error: node {} not added'.format(i))


network.get_node(0).hypercube.insert(7, res2['Hash'])
network.get_node(0).hypercube.insert(3, res1['Hash'])
print(network.get_node(0).hypercube.get_logic_node(3).get_cids())

print(network.get_node(0).hypercube.remove('QmXb9edthGYiMDRpr3y82u1daYgpdmewitArf1wTU46mCs'))
print(network.get_node(0).hypercube.get_logic_node(3).get_cids())

print()
print(list(node_1.swarm.addrs()['Addrs']))
print(len(list(node_1.swarm.addrs()['Addrs'])))
if node_2.id()['ID'] in list(node_1.swarm.addrs()['Addrs']):
    print('FOUND')


node_1.close()
node_2.close()





