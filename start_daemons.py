import subprocess
import os


POWERSHELL = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'

IPFS_PATH_1 = 'C:\\Users\\david\\.ipfs1'
IPFS_PATH_2 = 'C:\\Users\\david\\.ipfs2'


def start_daemon(ipfs_path):
    os.environ["IPFS_PATH"] = ipfs_path
    subprocess.Popen([POWERSHELL, '-ExecutionPolicy', 'Unrestricted', 'ipfs daemon'])


def kill_daemons():
    os.system("taskkill /IM ipfs.exe /F")


start_daemon(IPFS_PATH_1)
start_daemon(IPFS_PATH_2)

input()
kill_daemons()
