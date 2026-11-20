import random

def problem1(n):
    c = [[random.uniform(-100, 100) for i in range(n)] for j in range(n)]
    m, k = [], []
    for i in range(n):
        for j in range(n):
            if j > i:
                m.append(c[i][j])
            else:
                k.append(c[i][j])
    return m, k

def problem2(n):
