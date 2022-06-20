from re import L
from cypher import Heys
from random import randrange
from collections import Counter


heys = Heys()

# plainText = "0000111100001111"
# print("plain text: " + plainText)
# key = "0"+"1"*111
# print("key: " + key)
# cipherText = heys.encrypt(plainText, key)
# print(cipherText)

def list_xor(list1, list2):
    return [x1^x2 for x1, x2 in zip(list1, list2)]

def calcAlpha(alpha, attempt = 1_000_000):
    betas = []
    for i in range(attempt):
        key = [randrange(16),randrange(16),randrange(16),randrange(16)]
        beta = heys.round(alpha, key)
        betas.append(beta)
    counter = Counter(tuple(item) if type(item) is list else item for item in betas)
    print(counter.most_common(5))
    totalElements = sum([i[1] for i in counter.items()])
    print(totalElements)
    probabilities = [(i[0],i[1]/totalElements) for i in counter.items()]
    probabilities = sorted(probabilities, key=lambda item : item[1])
    print(probabilities[0:5])
    # fd = open('output', 'w')
    # fd.write(str(probabilities[0:5]))




def bruteforceAlpha():
    for i in range(16):
        for j in range(16):
            for k in range(16):
                for l in range(16):
                    calcAlpha([i,j,k,l])

def bruteforceDifference(difference):
    betas = []
    for i in range(16):
        for j in range(16):
            for k in range(16):
                for l in range(16):
                    text = [i,j,k,l]
                    betas.append(
                        list_xor(
                            heys.round(
                                text, 
                                [0,0,0,0]
                            ), 
                            heys.round(
                                list_xor(text, difference), 
                                [0,0,0,0]
                            ) 
                        )
                    )
    counter = Counter(tuple(item) for item in betas)
    return counter

# difference = [0,3,0,0]
# #calcAlpha(alpha)
# bruteforceDifference(difference)

def paralelBruteforceDifference():
    for i in range(4):
        difference = [0, 0, 0, 0]
        for j in range(15):
            difference[i] += 1
            bruteforceDifference(difference)
            print()



def diffSearch(alpha, prob):
    #betas = sorted([tuple([x[0], x[1] / 2**16]) for x in bruteforceDifference(alpha).items()], key=lambda x : -x[1])
    L = [[],[],[],[],[],[]]
    L[0] = [tuple([alpha, 1.0])]
    # f = list(filter(lambda x : x[0] == alpha , L[0] ))[0][1]
    # print(f)
    # print([tuple(l[0]) for l in L[0]])
    # print([0,0,0,1] in [tuple(l[0]) for l in L[0]])
    # print(L)
    for t in range(1,6):
        print(t)
        for (beta, p) in L[t-1]:
            gammas = sorted([tuple([x[0], x[1] / 2**16]) for x in bruteforceDifference(beta).items()], key=lambda x : -x[1])
            for (gamma, q) in gammas:
                # print(gamma)
                # print(q)
                if gamma in [tuple(l[0]) for l in L[t]]:
                    # print(f'found gamma {(gamma, q)}')
                    # print(L[t])
                    pg = list(filter(lambda x : x[0] == gamma , L[t]))[0][1]
                    L[t].remove((gamma, pg))
                    L[t].append((gamma, pg + p * q))
                else:
                    L[t].append(tuple([gamma, p * q]))
        L_t = L[t].copy()
        # for l in L_t:
        #     print(l)
        print(f'L[{t}] len: {len(L[t])}')
        for (gamma, p) in L[t]:
            if p <= prob:
                print(f'removed {(gamma, p)}')
                L_t.remove((gamma, p))
        L[t] = L_t.copy()
        # for l in L_t:
        #     print(l)
        print(f'L[{t}] len: {len(L[t])}')
    for L_t in L:
        for l in L_t:
            print(l)
        print()
    
    

alpha = [0,0,0,1]
prob = 0.0012
diffSearch(alpha, prob)

# L = [(alpha, prob)]
# L[0] = 1
# print(L)

# l = [[0,0,0,1],[0,0,0,1],[0,0,0,2]]
# a = Counter(tuple(item) if type(item) is list else item for item in l)
# print(a)
