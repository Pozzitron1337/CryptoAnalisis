from jinja2 import pass_environment

from settings import WORD_LEN
from settings import *

class Heys:
    def __init__(self):
        pass
        
    @staticmethod
    def encrypt(text: str, key: str):
        """
        args
            text - string of binary number. Length = BLOCK_LEN
            key - string of binary number. Length = KEY_LEN
        """

        keys = Heys.__split_key(key)
        print("keys: " + str(keys))
        bytes = Heys.__split_on_bytes(text)
        print("x = bytes0: " + str(bytes))

        rounds = len(keys) // WORD_LEN - 1 # 
        for round in range(rounds):
            bytes = Heys.__round(bytes, keys[round * WORD_LEN : (round + 1) * WORD_LEN])
            print(f'bytes{round+1}: {bytes}')
    
        bytes = Heys.__whitening(bytes, keys[rounds * WORD_LEN : (rounds+1) * WORD_LEN])
        return bytes
             
    @staticmethod
    def __round(text: int, key: int):
        """round function
        args
            text - array of 4 bit integer with len WORD_LEN
            key - array of 4 bit integer with len WORD_LEN
        """
        return Heys.__permutation(Heys.__substitution(Heys.__whitening(text, key)))
    
    
    @staticmethod
    def __whitening(bytes, key):
        return [bytes[i] ^ key[i] for i in range(WORD_LEN)]
    
    @staticmethod
    def __split_key(key: str):
        """
        args
            key - string of binary number. Length = KEY_LEN
        """
        return [int(key[i * WORD_LEN : (i+1) * WORD_LEN], 2) for i in range(len(key)//WORD_LEN)]
    
    
    @staticmethod
    def __split_on_bytes(block):
        """
        args
            block - string of binary number. Length = BLOCK_LEN
        """
        return [int(block[i * WORD_LEN: (i+1) * WORD_LEN], 2) for i in range(WORD_LEN)]
    
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