from .cypher import Heys
from random import randrange
from collections import Counter

heys = Heys()

def list_xor(list1, list2):
    return [x1^x2 for x1, x2 in zip(list1, list2)]


def bruteforceDifference(difference):
    betas = []
    for i in range(2**16):
        text = [(i >> 8) & 0xff, i & 0xff]
        X = heys.round(
                text, 
                [0x00,0x00]
            )
        X_ = heys.round(
            [text[0] ^ difference[0], text[1] ^ difference[1]],
            [0x00,0x00]
        ) 
        betas.append([ X[0] ^ X_[0], X[1] ^ X_[1]])

    counter = Counter(tuple(item) for item in betas)
    return counter

def diffSearch(alpha, P, r = 6):
    L = [[]] * r
    L[0] = [tuple([alpha, 1.0])]
    for t in range(1,r):
        print(t)
        for (beta, p) in L[t-1]:
            gammas = sorted([tuple([x[0], x[1] / 2**16]) for x in bruteforceDifference(beta).items()], key=lambda x : -x[1])
            for (gamma, q) in gammas:
                L_t = L[t].copy()
                if gamma in [tuple(l[0]) for l in L_t]:
                    pg = list(filter(lambda x : x[0] == gamma , L_t))[0][1]
                    L_t.remove((gamma, pg))
                    L_t.append((gamma, pg + (p * q)))
                else:
                    L_t.append(tuple([gamma, p * q]))
                L[t] = L_t.copy()
        
        print(f'L[{t}] prob: {sum([x[1] for x in L[t]])}')
        for l in sorted(L[t],key= lambda x: -x[1])[0:25]:
            print(l)
        print(f'L[{t}] len before: {len(L[t])}')
        L_t = L[t].copy()
        for (gamma, p) in L[t]:
            if p <= P[t]:
                L_t.remove((gamma, p))
        L[t] = L_t.copy()
        print(f'L[{t}] prob: {sum([x[1] for x in L[t]])}')
        for l in sorted(L[t],key= lambda x: -x[1])[0:25]:
            print(l)
        print(f'L[{t}] len after: {len(L[t])}')
       
    for t in range(len(L)):
        print(t)
        for l in sorted(L[t],key= lambda x : -x[1])[0:25]:
            print(l)
        print()
    



# alpha = [0x00, 0x01]
# #       1    2       3       4       5         6
# P = [1, 0.1, 0.0075, 0.005, 0.01, 0.001, 3.8e-06]
# P = [0.005]*7
# diffSearch(alpha, P, r = 6)
#print(bruteforceDifference(alpha))