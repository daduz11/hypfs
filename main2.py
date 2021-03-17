import ipfshttpclient
from src.parameters import *
from src.channel import Channel


def check(id, node):
    return id in list(node.swarm.addrs()['Addrs'])

# node 1: 12D3KooWDYSvSoJZn3HmJsK6fvVikeRKyGbqT7dueXZsGgLoLoJ5
# node 2: 12D3KooWJdRd7Gp6qLuzNrEJCgkP9MsvfQu7oqfgs6xYWKiS2wqV


node_2 = ipfshttpclient.connect(IPFS_CLIENT_ADDRESS_2)
print(node_2.id())
res2 = node_2.add('test2.txt')

print(check('12D3KooWDYSvSoJZn3HmJsK6fvVikeRKyGbqT7dueXZsGgLoLoJ5', node_2))

ch1 = Channel(node_2, 'hypercube_1')
ch2 = Channel(node_2, 'hypercube_2')

sender, msg_from_node1 = ch1.recv()
print(sender)
print(msg_from_node1)
ch2.send('hello from the node 2!')
sender, msg_from_node1 = ch1.recv()
print(msg_from_node1)


print(check('12D3KooWDYSvSoJZn3HmJsK6fvVikeRKyGbqT7dueXZsGgLoLoJ5', node_2))

node_2.close()





