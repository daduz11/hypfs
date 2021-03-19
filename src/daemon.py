import os
import subprocess
from datetime import datetime


class Daemon:
    def __init__(self, name, path, powershell=r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'):
        self.name = name.upper()
        self.path = path
        self.powershell = powershell
        self.daemon = None

    def log(self, msg):
        log_line = "> {} - [{}] -> {:<10}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), self.name, msg)
        print(log_line)

    def start_daemon(self):
        if self.daemon is None:
            os.environ["IPFS_PATH"] = self.path
            self.daemon = subprocess.Popen([self.powershell, '-ExecutionPolicy', 'Unrestricted', 'ipfs daemon --enable-pubsub-experiment'],
                                           stdout=subprocess.DEVNULL, shell=True, cwd=os.getcwd())
            self.log("DAEMON STARTED")
        else:
            self.log("DAEMON ALREADY RUNNING")

    def kill_daemon(self):
        if self.daemon is None:
            self.log("DAEMON NOT RUNNING")
        else:
            os.system("taskkill /F /PID " + str(os.getpid()))
            #self.daemon.send_signal(signal.CTRL_C_EVENT)
            #os.killpg(os.getpgid(self.daemon.pid), signal.SIGTERM)
            self.log("DAEMON STOPPED")
