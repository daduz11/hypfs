from src.parameters import *

class Search:
    def __init__(self, n_key, c_mex, number=None):
        self.n_key = n_key
        self.number = number
        self.check = False
        self.collect_id_bit = []
        self.cont = 0
        self.c_mex = c_mex

    def add_mex(self):
        self.c_mex += 1

    def get_N_mex(self):
        return self.c_mex

    def get_key(self):
        return self.n_key

    def get_number(self):
        return self.number

    def get_check(self):
        return self.check

    def set_check(self):
        self.check = True

    def add_cont(self):
        self.cont += 1

    def get_cont(self):
        return self.cont

    def remove_key(self):
        self.collect_id_bit.pop(0)

    def get_collect(self):
        return self.collect_id_bit

    def get_list_bit_refer(self, kw, hyper):
        id_bit = self.create_binary_id(kw, hyper)
        bit_1 = self.create_bitset(id_bit)
        for i in range(0, NETWORK_SIZE):
            continue ####################################################################################################################################################

