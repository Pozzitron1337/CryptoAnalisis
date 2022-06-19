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

def diffSearch(alpha):
    #betas = [tuple(x[0], x[1]/2**16) for x in bruteforceDifference(alpha).items()]
    betas = [tuple(x.key, x.value / 2**16) for x in bruteforceDifference(alpha)]
    print("betas:")
    print(betas)
    # for beta in betas:
    #     gammas = bruteforceDifference(beta[0]).most_common(3)
    #     print("gammas")
    #     print(gammas)
    #     # for gamma in gammas:
    #     #     deltas = bruteforceDifference(gamma[0]).most_common(3)
    #     #     print("deltas")
    #     #     print(deltas)
    #     #     for delta in deltas:
    #     #         epsilons = bruteforceDifference(delta[0]).most_common(3)
    #     #         print("epsilons")
    #     #         print(epsilons)
    #     #         for epsilon in epsilons:
    #     #             zetas = bruteforceDifference(epsilon[0]).most_common(3)
    #     #             print("zetas")
    #     #             print(zetas)
    #     #             for zeta
    

alpha = [0,0,0,1]
diffSearch(alpha)


# l = [[0,0,0,1],[0,0,0,1],[0,0,0,2]]
# a = Counter(tuple(item) if type(item) is list else item for item in l)
# print(a)
