import os
import signal
import subprocess
import sys

from src.config import INIT_PORT, HOP_SERVER_PORT
from src.utils import NODES, log

servers = [subprocess.Popen([sys.executable, 'hops_counter.py'])]
log('HOPS SERVER', 'STARTING', 'PORT {}'.format(str(HOP_SERVER_PORT)))

for pid in range(0, NODES):
    servers.append(subprocess.Popen([sys.executable, 'server.py', str(INIT_PORT + pid)]))
    log('SERVER {}'.format(str(pid)), 'STARTED', 'PORT {}'.format(str(INIT_PORT + pid)))
input()
for pid in servers:
    os.kill(pid.pid, signal.SIGTERM)
