import subprocess
import os

from src.utils import log

POWERSHELL = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'

IPFS_PATH_1 = 'C:\\Users\\david\\.ipfs1'
IPFS_PATH_2 = 'C:\\Users\\david\\.ipfs2'


def start_daemon(ipfs_path):
    os.environ["IPFS_PATH"] = ipfs_path
    subprocess.Popen(
        [POWERSHELL, '-ExecutionPolicy', 'Unrestricted', 'ipfs daemon'],
        stdout=subprocess.DEVNULL, shell=True, cwd=os.getcwd())
    log(ipfs_path.split('\\')[-1].split('.')[1].upper(), 'STARTED', '{}'.format(ipfs_path))


def kill_daemons():
    os.system("taskkill /IM ipfs.exe /F")


start_daemon(IPFS_PATH_1)
start_daemon(IPFS_PATH_2)

input('Press key to stop the daemons')

kill_daemons()