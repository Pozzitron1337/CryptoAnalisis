from jinja2 import pass_environment

from heys.settings import WORD_LEN
from .settings import *

class Heys:
    def __init__(self):
        self.__num_keys = 7
        
    # binary input
    @staticmethod
    def encrypt(text: str, key: str, num_rounds: int = 6):
        if len(key) != (num_rounds + 1 ) * BLOCK_LEN and len(text) != BLOCK_LEN:
            raise Exception()
        
        keys = Heys.__split_key(key)
        text = [int(i, 2) for i in Heys.__split_block(text)]
        
        for key in keys[:-1]:
            key_ = [int(i, 2) for i in key]
            text = Heys.__round(text, key_)
            
        key_ = [int(i, 2) for i in keys[-1]]
        return Heys.__whitening(text, key_)
        
        
    @staticmethod
    def __round(text, key):
        return Heys.__permutation(Heys.__substitution(Heys.__whitening(text, key)))
    
    
    @staticmethod
    def __whitening(text, key):
        text_ = [0 for i in range(WORD_LEN)]
        for i in range(WORD_LEN):
            text_ = text[i] ^ key[i]
        return text_
    
    
    @staticmethod
    def __split_key(key):
        return [Heys.__split_block(key[i: i + BLOCK_LEN]) for i in range(Heys.__num_keys)]
    
    
    @staticmethod
    def __split_block(block):
        return [block[i: i + WORD_LEN] for i in range(WORD_LEN)]
    
    
    @staticmethod
    def __permutation(text):
        new_text = [0 for i in range(WORD_LEN)]
        for i in range(WORD_LEN):
            for j in range(WORD_LEN):
                bin_w = bin(text[i])[2:]
                new_text[j] |= 0 if bin_w[j] == '0' else (1 >> i)
        return new_text
    
    
    @staticmethod
    def __substitution(text):
        return [S[i] for i in text]