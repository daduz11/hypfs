import ipfshttpclient
from src.parameters import *
from src.channel import Channel


def check(id, node):
    return id in list(node.swarm.addrs()['Addrs'])

# node 1: 12D3KooWDYSvSoJZn3HmJsK6fvVikeRKyGbqT7dueXZsGgLoLoJ5
# node 2: 12D3KooWJdRd7Gp6qLuzNrEJCgkP9MsvfQu7oqfgs6xYWKiS2wqV


node_1 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_1)
print(node_1.id())
res1 = node_1.add('test.txt')

print(check('12D3KooWJdRd7Gp6qLuzNrEJCgkP9MsvfQu7oqfgs6xYWKiS2wqV', node_1))

ch1 = Channel(node_1, 'hypercube_1')
ch2 = Channel(node_1, 'hypercube_2')

ch1.send('hello from the node 1!')
sender, msg_from_node2 = ch2.recv()
print(msg_from_node2)
ch1.send('hello from the node 1 again!')

print(check('12D3KooWJdRd7Gp6qLuzNrEJCgkP9MsvfQu7oqfgs6xYWKiS2wqV', node_1))

node_1.close()


def check(id, node):
    return id in list(node.swarm.addrs()['Addrs'])


