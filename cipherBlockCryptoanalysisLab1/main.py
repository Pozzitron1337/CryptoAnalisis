from calendar import c
from numpy import uint
from heys import Heys
import subprocess
from collections import Counter
from pprint import pprint
import threading
import concurrent.futures
import json


path = '/home/sovun/CryptoAnalisis/cipherBlockCryptoanalysisLab1'
byteorder = 'big'
key_ = f'{path}/key.bin'
# key_ = ""

num_threads = 8

def gen_ct(alpha_, texts):
    alpha = (alpha_[1] << 8) ^ alpha_[0]
    for text in texts:
        with open(f'{path}/pt.txt', 'wb') as pt:
            pt.write(int(text).to_bytes(2, byteorder))
        subprocess.Popen(f'{path}/heys.bin e 12 {path}/pt.txt {path}/ctexts/ct_{text}.bin {key_} >> /dev/null', stdin=subprocess.PIPE, shell=True).communicate(input="\x0a".encode())
        
        
        with open(f'{path}/pt.txt', 'wb') as pt:
            pt.write(int(text ^ alpha).to_bytes(2, byteorder))
        subprocess.Popen(f'{path}/heys.bin e 12 {path}/pt.txt {path}/ctexts/cta_{text}.bin {key_} >> /dev/null', stdin=subprocess.PIPE, shell=True).communicate(input="\x0a".encode())

def read_ct(texts):
    ctexts = []
    for text in texts:
        t1 = None
        with open(f'{path}/ctexts/ct_{text}.bin', 'rb') as f:
            t = f.read()
            t1 = [t[-1], t[-2]]
        
        t2 = None  
        with open(f'{path}/ctexts/cta_{text}.bin', 'rb') as f:
            t = f.read()
            t2 = [t[-1], t[-2]]
        
        ctexts.append([t1, t2])
        
    return ctexts

def get_beta(text1_, text2_, key):
    t1 = [text1_[0], text1_[1]]
    t2 = [text2_[0], text2_[1]]

    t1 = Heys.round_(t1, key)
    t2 = Heys.round_(t2, key)
    
    return ((t1[0] ^ t2[0]) << 8) ^ t1[1] ^ t2[1] 

def get_res(ctexts, beta, key):
    count = 0
    for text in ctexts:
        bt = get_beta(text[0], text[1], [(key >> 8) & 0xf, key & 0xf])
        if bt == beta:
            count += 1
    
    with open(f'{path}/res/{count}_{key}', 'a') as res_f:
        res_f.write(f'key: {[key & 0xf, (key >> 8) & 0xf]}, num: {count}\n')
        
def bruteforce(alpha_, beta_, keys, texts):
    # alpha = unite(alpha_)
    beta = (beta_[0] << 8) ^ beta_[1]
    
    # count = {}
    # gen_ct(alpha_, texts)
    ctexts = read_ct(texts)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for key in keys:
            futures.append(executor.submit(get_res, ctexts=ctexts, beta=beta, key=key))
    

# def bf(path, alpha_, beta_, texts):
#     alpha = unite(alpha_)
#     beta = unite(beta_)

#     count = {}
#     gen_ct(alpha, texts)
#     # key = 17546
#     key = 62097
#     for text in texts:
#         bt = get_beta(path, text, key)
#         if bt in count.keys():
#             count[bt] += 1 
#         else:
#             count[bt] = 1 
    
#     # with open(f'{path}/res_key', 'a') as res_f:
#     #     res_f.write(f'key: {key}, num: {count[key]}\n')  
                
#     return count   
        
if __name__ == "__main__":
    alpha = [0, 1]
    beta = [0, 5]
    texts = range(1, 1000)
    keys = range(2**15)
    # keys = range(2**15)
    # keys = range(2**15, 2**16)
    
    bruteforce(alpha, beta, keys, texts)
    
    # print(0x2f38)
    # 12088