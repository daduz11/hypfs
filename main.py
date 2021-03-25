import os
from random import randint
from statistics import mean

from client import Client
from src.config import LOCAL_HOST
from src.utils import request, HOP_SERVER_PORT, RESET_HOPS, GET_HOPS, reset_hops, get_hops, NODES


IPFS_CLIENT_ADDRESS = '/ip4/127.0.0.1/tcp/5001'
OBJECTS = 20
PINSEARCH_ATTEMPS = 20
SUPERSET_ATTEMPS = 20
SUPERSET_LIMIT = 10


client = Client(IPFS_CLIENT_ADDRESS, 7)


for i in range(0, OBJECTS):
    client = Client(IPFS_CLIENT_ADDRESS, randint(0, NODES-1))
    with open('./test_files/' + str(i), 'wb') as random_file:
        random_file.write(os.urandom(512))
    client.add_obj('./test_files/' + str(i), randint(0, NODES-1))
    client.close()

pinsearch_hops = []

for i in range(0, PINSEARCH_ATTEMPS):
    client = Client(IPFS_CLIENT_ADDRESS, randint(0, NODES-1))
    reset_hops()
    client.pin_search(randint(0, NODES-1))
    pinsearch_hops.append(get_hops())
    client.close()

superset_hops = []

for i in range(0, SUPERSET_ATTEMPS):
    client = Client(IPFS_CLIENT_ADDRESS, randint(0, NODES-1))
    reset_hops()
    client.superset_search(randint(0, NODES-1), SUPERSET_LIMIT)
    superset_hops.append(get_hops())
    client.close()

print()
print('RESULTS')
print('pinsearch: {}'.format(mean(pinsearch_hops)))
print('superset:  {}'.format(mean(superset_hops)))
