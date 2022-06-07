from jinja2 import pass_environment

from heys.settings import WORD_LEN
from .settings import *

class Heys:
    def __init__(self):
        self.__num_keys = 7
        
    # bytes input
    @staticmethod
    def encrypt(text: str, key: str, num_rounds: int = 6):
        if len(key) != (num_rounds + 1 ) * BLOCK_LEN and len(text) != BLOCK_LEN:
            raise Exception()
        
        keys = Heys.__split_on_bytes(key)
        bytes = Heys.__split_on_bytes(text)
        
        for i in range(num_rounds - 1):
            key_ = key[i*WORD_LEN: (i+1)* WORD_LEN]
            bytes = Heys.__round(bytes, key_)
            
        key_ = [int(i, 2) for i in keys[-1]]
        return Heys.__whitening(text, key_)
        
        
    @staticmethod
    def __round(text, key):
        return Heys.__permutation(Heys.__substitution(Heys.__whitening(text, key)))
    
    
    @staticmethod
    def __whitening(bytes, key):
        return [bytes[i] ^ key[i] for i in range(WORD_LEN)]
    
    
    # @staticmethod
    # def __split_key(key):
    #     return [Heys.__split_block(key[i: i + BLOCK_LEN]) for i in range(Heys.__num_keys)]
    
    
    @staticmethod
    def __split_on_bytes(block):
        return [int(block[i*WORD_LEN: (i+1)*WORD_LEN], 2) for i in range(WORD_LEN)]
    
    @staticmethod
    def __permutation(bytes):
        new_text = [0 for i in range(WORD_LEN)]
        for i in range(WORD_LEN):
            for j in range(WORD_LEN):
                new_text[WORD_LEN - 1 - j] |= 0 if Heys.__get_bit(bytes[i], j) == 0 else (1 << (WORD_LEN - 1 - i))
        return new_text


    @staticmethod
    def __get_bit(num, ind: int):
        return num & (0x1 << ind)
    
    
    @staticmethod
    def __substitution(bytes):
        return [S[i] for i in bytes]
    
if __name__ == "__main__" :
    print(Heys.__permutation("0101010101010101"))