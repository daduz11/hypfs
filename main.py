import ipfshttpclient
from src.parameters import *
import requests
from flask import Response

from src.utils import request, create_binary_id

client_1 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_1)
client_2 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_2)

res1 = client_1.add('test.txt')
res2 = client_2.add('test2.txt')


print(client_1.id()) #12D3KooWDYSvSoJZn3HmJsK6fvVikeRKyGbqT7dueXZsGgLoLoJ5
print(client_2.id()) #12D3KooWJdRd7Gp6qLuzNrEJCgkP9MsvfQu7oqfgs6xYWKiS2wqV

print()
#print(node_1.dht.findpeer(node_2.id()['ID'])) #cerca nella DHT il nodo con ID passato
#print(node_1.dht.findprovs(res2['Hash'])) #cerca nella DHT i nodi che possono fornire l'oggetto il cui hash passato
"""
params = {'keyword': str(1), 'object': 'object_1'}
url = "http://{}:{}/insert".format(LOCAL_HOST, '50000')  # + int(next_node, 2))
print(url)
r = requests.get(url=url, params=params)
"""
request(create_binary_id(0), INSERT, str(1), 'object_1')
#request(create_binary_id(0), REMOVE, str(1), 'object_1')
res = request(create_binary_id(0), PIN_SEARCH, str(1), None)
print(res.text)

"""
hypercube.insert(7, res2['Hash'])
hypercube.insert(3, res1['Hash'])
print('cids dict', hypercube.get_logic_node(7).get_objects())
#print('graph', network.get_node(0).hypercube.plot_graph())
print('pinsearch dict', hypercube.pin_search(3))
print('superset dict', hypercube.superset_search(3))
#print('remove from dict', network.get_node(0).hypercube.remove('QmXb9edthGYiMDRpr3y82u1daYgpdmewitArf1wTU46mCs'))
#print('cids after remove from dict', network.get_node(0).hypercube.get_logic_node(3).get_cids())

print()
"""
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





