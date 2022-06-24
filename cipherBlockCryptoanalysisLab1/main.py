from numpy import uint
from heys import Heys
import subprocess
from collections import Counter
from pprint import pprint
import json


path = '/mnt/d/Documents/linux/CryptoAnalisis/cipherBlockCryptoanalysisLab1'
byteorder = 'little'
# key_ = f'{path}/key.bin'
key_ = ""

def gen_ct(alpha, nums):
    # alpha = unite(alpha_)
    for text in nums:
        with open(f'{path}/pt.txt', 'wb') as pt:
            pt.write(int(text).to_bytes(2, byteorder))
        subprocess.Popen(f'{path}/heys.bin e 12 {path}/pt.txt {path}/ctexts/ct_{text}.bin {key_}', stdin=subprocess.PIPE, shell=True).communicate(input="\x0a".encode())
        
        
        with open(f'{path}/pt.txt', 'wb') as pt:
            pt.write(int(text ^ alpha).to_bytes(2, byteorder))
        subprocess.Popen(f'{path}/heys.bin e 12 {path}/pt.txt {path}/ctexts/cta_{text}.bin {key_}', stdin=subprocess.PIPE, shell=True).communicate(input="\x0a".encode())
        

def split(i):
    return [(i>>12) & 0xf, (i >>8) & 0xf, (i >>4) & 0xf, i & 0xf]

def unite(vec):
    x = 0
    l = len(vec)
    for i in range(l):
        x |= vec[i] << (l - i - 1) * 4
    return x

def get_beta(path, num, key):
    t1 = 0
    with open(f'{path}/ctexts/ct_{num}.bin', 'rb') as pt:
        t1 = pt.read()
    t1 = Heys.round_(split(int.from_bytes(t1, byteorder) ^ key))
    
    t2 = 0 
    with open(f'{path}/ctexts/cta_{num}.bin', 'rb') as pt:
        t2 = pt.read()
    t2 = Heys.round_(split(int.from_bytes(t2, byteorder) ^ key))
    
    return unite(t1) ^ unite(t2) 
        
    

def bruteforce(path, alpha_, beta_, texts):
    alpha = unite(alpha_)
    beta = unite(beta_)
    
    count = {}
    gen_ct(alpha, texts)
    for key in range(1, 2**16):
        count[key] = 0
        for text in texts:
            bt = get_beta(path, text, key)
            if bt == beta:
                count[key] += 1  
        
        with open(f'{path}/res_key', 'a') as res_f:
            res_f.write(f'key: {key}, num: {count[key]}\n')  
                
    return count      
        
if __name__ == "__main__":
    alpha = [0, 3, 0, 0]
    beta = [0, 1, 0, 1]
    texts = range(1, 500)
    
    res = bruteforce(path, alpha, beta, texts)