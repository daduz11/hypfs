from datetime import datetime
import requests

from src.config import LOCAL_HOST, HYPERCUBE_SIZE, INIT_PORT, HOP_SERVER_PORT

NODES = 2 ** HYPERCUBE_SIZE
INSERT = '/insert'
REMOVE = '/remove'
PIN_SEARCH = '/pin_search'
SUPERSET_SEARCH = '/superset_search'
INCREASE_HOPS = '/increase_hops'
RESET_HOPS = '/reset_hops'
GET_HOPS = '/get_hops'


def request(neighbor, operation, params={}):
    increase_hops()
    url = "http://{}:{}{}".format(LOCAL_HOST, str(get_decimal(neighbor) + INIT_PORT), operation)
    return requests.get(url=url, params=params)


def increase_hops():
    requests.get(url="http://{}:{}{}".format(LOCAL_HOST, HOP_SERVER_PORT, INCREASE_HOPS))


def reset_hops():
    requests.get(url="http://{}:{}{}".format(LOCAL_HOST, HOP_SERVER_PORT, RESET_HOPS))


def get_hops():
    return int(requests.get(url="http://{}:{}{}".format(LOCAL_HOST, HOP_SERVER_PORT, GET_HOPS)).text) - 1


def create_binary_id(n):
    binary_id = bin(n)[2:]
    while len(binary_id) < HYPERCUBE_SIZE:
        binary_id = '0' + binary_id
    return binary_id


def get_decimal(bit):
    return int(bit, 2)


def one(bit):
    n = get_decimal(bit)
    return [i for i in range(0, len(bit)) if n & (1 << i)]


def hamming_distance(n1, n2):
    x = n1 ^ n2
    set_bits = 0
    while x > 0:
        set_bits += x & 1
        x >>= 1
    return set_bits


def log(tid, operation, msg):
    log_line = "> {} - [{}] -> [{}]: {:20}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), tid, operation.upper(), msg)
    print(log_line)
    return


def get_response(res):
    if res != '':
        return res.split(',')
    else:
        return []
