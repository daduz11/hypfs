import argparse
import sys
from flask import Flask, request
from src.node import Node
from src.parameters import APP_NAME, LOCAL_HOST, INIT_PORT
app = Flask(APP_NAME)


@app.route('/insert')
def request_insert():
    keyword = int(request.args.get('keyword'))
    obj = request.args.get('obj')
    res = NODE.insert(keyword, obj)
    if type(res) is not str:
        res = res.text
    return res


@app.route('/remove')
def request_remove():
    keyword = int(request.args.get('keyword'))
    obj = request.args.get('obj')
    res = NODE.remove(keyword, obj)
    if type(res) is not str:
        res = res.text
    return res


@app.route('/pin_search')
def request_pin_search():
    keyword = int(request.args.get('keyword'))
    threshold = request.args.get('threshold')
    if threshold is None:
        res = NODE.pin_search(keyword)
    else:
        res = NODE.pin_search(keyword, int(threshold))
    if type(res) is not list:
        res = res.text
    else:
        res = ','.join(res)
    return res


@app.route('/superset_search')
def request_superset_search():
    keyword = int(request.args.get('keyword'))
    threshold = int(request.args.get('threshold'))
    superset = request.args.get('superset')
    res = NODE.superset_search(keyword, threshold, superset)
    if type(res) is not list:
        res = res.text
    else:
        res = ','.join(res)
    return res


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='Port number to which connect the node')
    return parser.parse_args(argv)


if __name__ == '__main__':
    PORT = parse_arguments(sys.argv[1:]).port
    NODE_ID = PORT - INIT_PORT
    NODE = Node(NODE_ID)

    app.run(host=LOCAL_HOST, port=PORT, threaded=True)
