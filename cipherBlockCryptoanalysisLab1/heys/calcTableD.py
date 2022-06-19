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
    print(f"alpha: {difference}") 
    print(counter)

alpha = [0,3,0,0]
#calcAlpha(alpha)
bruteforceDifference(alpha)

# l = [[0,0,0,1],[0,0,0,1],[0,0,0,2]]
# a = Counter(tuple(item) if type(item) is list else item for item in l)
# print(a)
