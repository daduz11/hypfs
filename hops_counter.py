from flask import Flask
from src.utils import *

app = Flask('hops_counter')
HOPS = 0


@app.route(INCREASE_HOPS)
def increase_hops():
    global HOPS
    HOPS += 1
    print(HOPS)
    return 'success'


@app.route(RESET_HOPS)
def reset_hops():
    global HOPS
    HOPS = 0
    return 'success'


@app.route(GET_HOPS)
def get_hops():
    return str(HOPS)


if __name__ == '__main__':
    app.run(host=LOCAL_HOST, port=HOP_SERVER_PORT, threaded=True)
