import argparse
import sys
from flask import Flask, request, Response, jsonify
from src.node import Node
from src.parameters import APP_NAME, LOCAL_HOST, INIT_PORT
app = Flask(APP_NAME)


@app.route('/insert')
def request_insert():
    keyword = int(request.args.get('keyword'))
    object = request.args.get('object')
    NODE.insert(keyword, object)
    print(NODE.get_objects())
    return 'success'


@app.route('/remove')
def request_remove():
    keyword = int(request.args.get('keyword'))
    object = request.args.get('object')
    NODE.remove(keyword, object)
    print(NODE.get_objects())
    return 'success'


@app.route('/pin_search')
def request_pin_search():
    keyword = int(request.args.get('keyword'))
    res = NODE.pin_search(keyword)
    if type(res) is not list:
        res = res.text
    return str(res)


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='an integer for the accumulator')
    return parser.parse_args(argv)


if __name__ == '__main__':
    PORT = parse_arguments(sys.argv[1:]).port
    NODE_ID = PORT - INIT_PORT
    NODE = Node(NODE_ID)

    app.run(host=LOCAL_HOST, port=PORT, threaded=True)
