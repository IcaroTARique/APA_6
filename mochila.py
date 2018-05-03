#!/usr/bin/python3.5
#coding: utf-8
def mochila(M, peso, valor, n):
    K = [[0 for x in range(M+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(M+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif peso[i-1] <= w:
                K[i][w] = max(valor[i-1] + K[i-1][w-peso[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][M]

for i in range(6+1):
    valor = [3,4,5,3]
    peso = [3,2,4,3]
    M = i
    n = len(valor)
    print(mochila(M, peso, valor, n))