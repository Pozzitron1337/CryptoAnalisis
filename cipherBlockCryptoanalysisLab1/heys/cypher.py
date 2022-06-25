from .settings import WORD_LEN
from .settings import *

class Heys:
    def __init__(self):
        pass
        
    @staticmethod
    def encrypt(bytes_, keys_):
        """
        args
            text - string of binary number. Length = BLOCK_LEN
            key - string of binary number. Length = KEY_LEN
        """
        bytes = [bytes_[1], bytes_[0]]
        keys = [[keys_[i*2 +1], keys_[i*2]] for i in range(7)]
        # print(f'bytes{bytes}\n\n')
        # keys = Heys.__split_key(key)
        # print("keys: " + str(keys))
        # bytes = Heys.__split_on_bytes(text)
        # print("x = bytes0: " + str(bytes))

        rounds = 7 # 
        for round in range(rounds - 1):
            # print(f'round: {round +1}')
            # print(f'bytes: {Heys.__tohex(bytes)}')
            # print(f'key: {Heys.__tohex(keys[round])}')
            
            bytes = Heys.round(bytes, keys[round])
            # print(f'bytes: {Heys.__tohex(bytes)}\n\n')

        # print(f'key: {Heys.__tohex(keys[-1])}') 
        bytes = Heys.__whitening(bytes, keys[-1])
        # print(f'bytes: {Heys.__tohex(bytes)}\n\n')
        return [bytes[1], bytes[0]]

    @staticmethod
    def round(text: int, key: int):
        """round function
        args
            text - array of 4 bit integer with len WORD_LEN
            key - array of 4 bit integer with len WORD_LEN
        """
        # t1 = Heys.__whitening(text, key)
        # print(f'whitening: {Heys.__tohex(t1)}')
        
        # t2 = Heys.substitution(t1)
        # print(f'substitution: {Heys.__tohex(t2)}')
        
        # t3 = Heys.permutation(t2)
        # print(f'permutation: {Heys.__tohex(t3)}')
        
        # return t3
        
        return Heys.permutation(Heys.substitution(Heys.__whitening(text, key)))
    
    @staticmethod
    def round_(text, key):
        """round function
        args
            text - array of 4 bit integer with len WORD_LEN
            key - array of 4 bit integer with len WORD_LEN
        """
        return Heys.substitution_(Heys.permutation(Heys.__whitening(text, key)))
    
    
    @staticmethod
    def __whitening(bytes, key):
        # print(f'whitening: {Heys.__tohex([bytes[0] ^ key[0], bytes[1] ^ key[1]])}')
        return [bytes[0] ^ key[0], bytes[1] ^ key[1]]
    
    # @staticmethod
    # def __split_key(key: str):
    #     """
    #     args
    #         key - string of binary number. Length = KEY_LEN
    #     """
    #     return [int(key[i * WORD_LEN : (i+1) * WORD_LEN], 2) for i in range(len(key)//WORD_LEN)]
    
    
    # @staticmethod
    # def __split_on_bytes(block):
    #     """
    #     args
    #         block - string of binary number. Length = BLOCK_LEN
    #     """
    #     return [int(block[i * WORD_LEN: (i+1) * WORD_LEN], 2) for i in range(WORD_LEN)]
    
    # @staticmethod
    # def __permutation(bytes):
    #     new_text = [0 for i in range(WORD_LEN)]
    #     for i in range(WORD_LEN):
    #         for j in range(WORD_LEN):
    #             new_text[WORD_LEN - 1 - j] |= 0 if Heys.__get_bit(bytes[i], j) == 0 else (1 << (WORD_LEN - 1 - i))
    #     return new_text
    
    @staticmethod
    def __tohex(data):
        return [hex(data[0]), hex(data[1])]
        
    @staticmethod
    def __split(bytes):
        return [(bytes[0] >> WORD_LEN) & 0xf, bytes[0] & 0xf, (bytes[1] >> WORD_LEN) & 0xf, bytes[1] & 0xf]
    
    @staticmethod
    def __unite(vec):
        # x = [(vec[0] << WORD_LEN) ^ vec[1], (vec[2] << WORD_LEN) ^ vec[3]]
        return [(vec[0] << WORD_LEN) ^ vec[1], (vec[2] << WORD_LEN) ^ vec[3]]

    @staticmethod
    def permutation(bytes_):
        bytes = Heys.__split(bytes_)
        new_text = [0, 0, 0, 0]
        for i in range(WORD_LEN):
            for j in range(WORD_LEN):
                new_text[WORD_LEN - 1 - j] |= 0 if Heys.__get_bit(bytes[i], j) == 0 else (1 << (WORD_LEN - 1 - i))
                
        return Heys.__unite(new_text)


    @staticmethod
    def __get_bit(num, ind: int):
        return num & (0x1 << ind)
    
    
    @staticmethod
    def substitution(bytes):
        return [(S[(bytes[0] >> WORD_LEN) & 0xf] << WORD_LEN)  ^ S[bytes[0] & 0xf], ( S[(bytes[1] >> WORD_LEN) & 0xf] << WORD_LEN) ^ S[bytes[1] & 0xf]]
    
    @staticmethod
    def substitution_(bytes):
        return [(S_[(bytes[0] >> WORD_LEN) & 0xf] << WORD_LEN) ^ S_[bytes[0] & 0xf], (S_[(bytes[1] >> WORD_LEN) & 0xf] << WORD_LEN) ^ S_[bytes[1] & 0xf]]
    
if __name__ == "__main__" :
    print(Heys.__permutation("0101010101010101"))