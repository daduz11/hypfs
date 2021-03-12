from src.parameters import HYPERCUBE_SIZE
import math

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

def get_binary_combination(keyword):
    bitset = create_bitset(create_binary_id(keyword))
    combinations = generate_binary_combination(HYPERCUBE_SIZE)
    result = []
    for combination in combinations:
        check = True
        for position in bitset:
            if combination[HYPERCUBE_SIZE - position - 1] != '1':
                check = False
                break
        if check:
            result.append(combination)
    return result


# dato un intero n, restituisce tutte le combinazioni di n bit
def generate_binary_combination(n):
  bin_arr = range(0, int(math.pow(2,n)))
  bin_arr = [bin(i)[2:] for i in bin_arr]
  max_len = len(max(bin_arr, key=len))
  bin_arr = [i.zfill(max_len) for i in bin_arr]

  return bin_arr

