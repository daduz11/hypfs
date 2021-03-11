from src.parameters import HYPERCUBE_SIZE

# trasformo il numero del nodo nel corrispondente in binario

def create_binary_id(n):
    # se il codice binario del nodo ottenuto non è della lunghezza r (dimensione dell'ipercubo) allora aggiungo gli zeri necessari
    binary_id = bin(n)[2:]
    while len(binary_id) < HYPERCUBE_SIZE:
        binary_id = '0' + binary_id
    return binary_id

# dato in input l'id del nodo si ottiene un bitset dove si tiene traccia dei bit ad 1
def create_bitset(id):
    n = int(id, 2)
    return [i for i in range(n.bit_length()) if n & (1 << i)]
