from collections import deque

G = [[]]
N = 1


# bfs
def bfs(start: int) -> list:
    dist = [-1 for i in range(N + 1)]
    dist[start] = 0
    dq = deque([start])
    while len(dq) > 0:
        pos = dq[0]
        dq.popleft()
        for nex in G[pos]:
            if dist[nex] < 0:
                dist[nex] = dist[pos] + 1
                dq.append(nex)
    # dist[1:]がスタートからの距離を表す
    return dist[1:]


# bfs
def bfs_fast(start: int) -> list:
    dist = {}
    dist[start] = 0
    dq = deque([start])
    while len(dq) > 0:
        pos = dq[0]
        dq.popleft()
        for nex in G[pos]:
            if not nex in dist:
                dist[nex] = dist[pos] + 1
                dq.append(nex)
    # distがスタートからの距離を表す,到達可能な点のみ
    return dist
