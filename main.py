from random import randint

from src.client import Client

IPFS_CLIENT_ADDRESS_1 = '/ip4/127.0.0.1/tcp/5001'
IPFS_CLIENT_ADDRESS_2 = '/ip4/127.0.0.1/tcp/5002'

client_1 = Client(IPFS_CLIENT_ADDRESS_1, 7)
client_2 = Client(IPFS_CLIENT_ADDRESS_1, 1)




hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',1)
hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',2)
hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',3)
hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',4)
hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',5)
hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',6)
hash_1 = client_1.add_obj('F:\\david\\Google Drive\\Documents\\uni\\BC\\project\\cappuccetto_rotto.txt',7)
client_1.remove_obj('QmXb9edthGYiMDRpr3y82u1daYgpdmewitArf1wTU46mCs', 5)
client_1.pin_search(3)
client_1.superset_search(1)

client_1.get_obj(input())

print()

client_1.close()
