


def differentialSearch(alpha, probability, rounds: int, delta: list = []):
    L = [[] for i in range(rounds)]
    L[0] = [[alpha, probability]]
    print(L)
    for round in range(1, rounds):
        for [b, p] in L[round-1]:
            for [g, q] in delta[round - 1]:
                x = list(map(lambda x: x[0],L[round]))
                if g in x:
                    print(x)
                    i = x.index(g)
                    L[round][i][1] += p * q
                else:
                    L[round].append([g, p * q])
        print(L)
        L[round] = [l for l in L[round] if not (l[1] < probability)]
        print(L)
    print(L)

        
rounds = 4
delta = [
        [[1, 0.2], [3, 0.5]], 
        [[3, 0.3]], 
        [], 
        []
        ]
differentialSearch(3, 0.5, rounds=rounds, delta=delta)