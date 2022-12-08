import heapq
from collections import deque

G = [[] for i in range(N + 1)]
input_edge = [0] * (N + 1)
for i in range(M):
    G[A[i]].append(B[i])
    input_edge[B[i]] += 1

for i in range(1, N + 1):
    G[i].sort()


def topological_sort(G, into_num):

    # 入ってくる有向辺を持たないノードを列挙
    q = deque()
    for i in range(1, len(into_num)):
        if into_num[i] == 0:
            q.append(i)

    # 以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1  # 入次数を減らす
            if into_num[adj] == 0:
                q.append(adj)  # 入次数が0になったら、キューに入れる

    return ans


def topological_dict_sort(node, input_edge):
    """トポロジカルソート(辞書順)

    有向グラフの順序を守るようにソートする
    閉路があるか判定も出来る
    計算量: O(E+V)

    Args:
        node (list): edge[i] = [a, b,...] iからa,b,...に辺が伸びている
        input_edge (list): input_edge[i] = iの入力辺の本数

    Returns:
        list or -1:閉路が存在しないとき
                      ソート済みのリスト
                   閉路が存在する時
                      -1
    """
    N = len(input_edge) - 1
    ans = []
    que = [i + 1 for i in range(N) if input_edge[i + 1] == 0]
    heapq.heapify(que)
    while que:
        q = heapq.heappop(que)
        ans.append(q)
        for e in node[q]:
            input_edge[e] -= 1
            if input_edge[e] == 0:
                heapq.heappush(que, e)

    if len(ans) == N:
        return ans
    return -1
