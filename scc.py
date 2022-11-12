"""強連結成分（閉路部分）を検出し、その構成要素数を閉路部分ごとに全列挙 O(N+M)"""


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
A = [0 for i in range(M)]
B = [0 for i in range(M)]
for i in range(M):
    A[i], B[i] = map(int, input().split())

# SCCを行い閉路部分の要素数を全列挙

# データ格納
outG = [[] for i in range(N + 1)]
inG = [[] for i in range(N + 1)]
for i in range(M):
    outG[A[i]].append(B[i])
    inG[B[i]].append(A[i])


def dfs(v, visited):
    global tmp
    global nums

    visited[v] = True
    for nex in outG[v]:
        if not visited[nex]:
            dfs(nex, visited)
    tmp += 1
    nums[v] = tmp


def l_sort(a: list, b: list) -> list:
    """b順に昇順ソートしたaを返す"""
    indx = [i for i in range(len(a))]
    indx.sort(key=lambda x: b[x])
    ret = []
    for i in range(len(indx)):
        ret.append(a[indx[i]])
    return ret


def dfs2(v):
    global visited
    visited[v] = True
    global max_dist

    for nex in inG[v]:
        if not visited[nex]:
            max_dist += 1
            dfs2(nex)


# 帰りがけ順に番号を記録
tmp = 0
visited = [False for i in range(N + 1)]
nums = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited)
nums = nums[1:]
nodes = [i + 1 for i in range(N)]

# 番号順に頂点を降順ソート
nodes = l_sort(nodes, nums)
nodes.reverse()

# 辺の向きを反対にしdfsで最大距離を順に記録
ans = []
max_dist = 1
visited = [False for i in range(N + 1)]
for i in nodes:
    if not visited[i]:
        dfs2(i)
        ans.append(max_dist)
        max_dist = 1

# ansが求める解
