from src.Node import Node
import os
IPFS_PATH_1 = 'C:\\Users\\david\\.ipfs1'
IPFS_PATH_2 = 'C:\\Users\\david\\.ipfs2'

daemon1 = Node('node1', IPFS_PATH_1)
daemon2 = Node('node2', IPFS_PATH_2)

daemon1.start_daemon()
daemon2.start_daemon()

input()
os.system("taskkill /IM ipfs.exe /F")

#daemon1.kill_daemon()
#daemon2.kill_daemon()
