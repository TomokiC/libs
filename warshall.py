import io
import math
import string
import sys

# import numpy as np

# 全点対最短経路問題

_INPUT = """5 9
1 2 3
1 3 8
1 5 -4
2 5 7
2 4 1
3 2 4
4 3 -5
4 1 2
5 4 6

"""
sys.stdin = io.StringIO(_INPUT)


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split(" "))
A = [0 for i in range(M)]
B = [0 for i in range(M)]
D = [0 for i in range(M)]
for i in range(M):
    A[i], B[i], D[i] = map(int, input().split(" "))

# 距離行列
f_inf = float("inf")
C = [[f_inf for i in range(N)] for i in range(N)]
# 同要素同士は距離0
for i in range(N):
    C[i][i] = 0
# 辺の長さが与えられた部分には値を代入
for i in range(M):
    C[A[i] - 1][B[i] - 1] = D[i]


def floyd_warshall(C):
    for k in range(N):
        for j in range(N):
            for i in range(N):
                if C[i][k] != f_inf and C[k][j] != f_inf:
                    C[i][j] = min(C[i][j], C[i][k] + C[k][j])
    return C


print(floyd_warshall(C))
