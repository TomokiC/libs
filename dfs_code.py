import copy
import io
import math
import string
import sys

# 有向グラフで探索可能なルートを深さ優先探索で全て出力

# 入力　頂点の数、辺の始点、終点
_INPUT = """\
6 5
1 2
1 3
3 4
3 5
2 5

"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
nodes = [list(map(int, input().split())) for i in range(M)]

tables = [[0] * N for i in range(N)]
for i in range(len(nodes)):
    tables[nodes[i][0] - 1][nodes[i][1] - 1] = 1

res = []

G = [[] for i in range(N)]
# for i in range(M):
#     G[]

circle = False


def dfs(v, visited, before_v):
    """グラフで閉路があるか検出"""
    global circle
    visited[v] = True
    for nex in G[v]:
        if visited[nex]:
            # 探索済み頂点に到達しかつひとつ前に訪問した頂点でなければ閉路ありと判定
            if nex != before_v:
                circle = True
        else:
            dfs(nex, visited, v)


def search_branch(start):
    """始点から次に移動可能な頂点を全て探索"""
    idx = -1
    result = []
    for cnt in range(tables[start][:].count(1)):
        idx = tables[start][:].index(1, idx + 1)
        result.append(idx)
    return result


def dfs(v, visited, roots):
    """グラフで経路探索で経路を記録"""
    visited[v - 1] = True
    roots.append(v)
    if v == Y:
        print(*roots)
    for nex in G[v - 1]:
        if not visited[nex - 1]:
            dfs(nex, visited, roots)
    roots.pop()


# 全頂点、全長さを探索
# for start_ in range(0, N):
#     for length_ in range(1, N):
#         A = []
#         dfs_all(A)

# 有向グラフを無向グラフに変換
# for i in range(N):
#     for j in range(i + 1, N):
#         if tables[i][j] == 1 or tables[j][i] == 1:
#             tables[i][j] = 1
#             tables[j][i] = 1


visited = [0] * N


def dfs_conneted(v):
    """グラフで全頂点の接続を判定"""
    # 深さ優先探索ですべての頂点が連結されているか判定
    # 頂点 v を訪問済みにする
    visited[v] = 1
    for v2 in range(N):
        # 頂点 v と頂点 v2 との結合が無い場合
        if tables[v][v2] == 0:
            continue
        # v2 は訪問済みの場合
        if visited[v2] == 1:
            continue
        dfs_conneted(v2)


dfs_conneted(0)
print(visited)
