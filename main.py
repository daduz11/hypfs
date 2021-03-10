import ipfshttpclient
from src.Insert import Insert
from src.Search import Search

node_1 = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
node_2 = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5002')

res1 = node_1.add('test.txt')
res2 = node_2.add('test.txt')

print(node_1.id())
print(node_2.id())

insert = Insert('123', 'ciao')

print(insert.get_keyword())
print(insert.get_hash_obj())

search = Search(1,1)
bit_id = search.create_binary_id(5, 4)
print(bit_id)
bitset = search.create_bitset(bit_id)
print(bitset)





