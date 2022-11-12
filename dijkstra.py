import heapq
import io
import math
import string
import sys

# import numpy as np

# _INPUT = """15 30
# 10 11 23
# 11 13 24
# 5 8 22
# 10 15 18
# 12 14 15
# 2 10 11
# 4 7 15
# 5 7 15
# 7 9 8
# 8 12 1
# 5 14 1
# 10 14 17
# 10 12 11
# 8 10 6
# 7 14 28
# 6 9 1
# 1 10 19
# 4 5 4
# 9 10 21
# 7 10 21
# 4 10 29
# 5 10 8
# 4 14 8
# 11 12 24
# 10 13 13
# 3 10 1
# 5 12 24
# 2 15 23
# 6 10 18
# 6 15 25


# """
# sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
A = [0 for i in range(M)]
B = [0 for i in range(M)]
C = [0 for i in range(M)]
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())

G = [[] for i in range(N + 1)]
for i in range(M):
    G[A[i]].append((B[i], C[i]))
    G[B[i]].append((A[i], C[i]))

# ダイクストラ法
def Dijkstra(start, G):

    # スタート地点からの距離
    INF = 10**12

    Label = [INF for i in range(N + 1)]
    Label[start] = 0

    # 訪問済みかどうかのフラグ
    visited = [False for i in range(N + 1)]
    pos = start

    # 優先度つきキューに(距離、頂点番号を記録)
    Q = []
    heapq.heappush(Q, (Label[start], start))

    while len(Q) >= 1:
        # 未訪問の頂点のうち始点からの距離（ラベル値が）最小の点を選択
        pos = heapq.heappop(Q)[1]
        if visited[pos]:
            continue

        # 探索済みフラグ
        visited[pos] = True
        # 隣接頂点のラベルを更新
        for e in G[pos]:
            if Label[e[0]] > Label[pos] + e[1]:
                Label[e[0]] = Label[pos] + e[1]
                heapq.heappush(Q, (Label[e[0]], e[0]))

    return Label


label = Dijkstra(1, G)
for i in range(1, N + 1):
    if label[i] == 10**12:
        print(-1)
    else:
        print(label[i])
