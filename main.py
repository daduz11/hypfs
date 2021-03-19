import ipfshttpclient
from src.parameters import *

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
request(create_binary_id(0), INSERT, {'keyword': str(0), 'obj': 'object_0'})
request(create_binary_id(0), INSERT, {'keyword': str(1), 'obj': 'object_1'})
request(create_binary_id(0), INSERT, {'keyword': str(2), 'obj': 'object_2'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_3'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_4'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_5'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_6'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_7'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_8'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_9'})
request(create_binary_id(0), INSERT, {'keyword': str(3), 'obj': 'object_10'})

#request(create_binary_id(0), REMOVE, str(1), 'object_1')
#res = request(create_binary_id(0), PIN_SEARCH, {'keyword': str(1)})
#print('pinsearch', res.text.split(','))

res = request(create_binary_id(0), SUPERSET_SEARCH, {'keyword': str(3), 'threshold': 2})
print('superset', res.text.split(','))

#res = request(create_binary_id(0), PIN_SEARCH, {'keyword': str(1)})
#print('pinsearch', res.text.split(','))


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





