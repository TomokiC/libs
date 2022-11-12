G = [[], [2, 4], [3, 5], [], [6], [], []]


def dfs(v, visited, ret, node):
    visited[v] = True
    # vに直前の点から向かう辺の長さを記録
    ret.append(v)
    for nex in G[v]:
        node.append(v)
        if not visited[nex]:
            dfs(nex, visited, ret, node)
    # vから親に向かう辺の長さを記録
    ret.append(-1 * v)
    node.append(v)

    return ret, node


def Euler_tour(root: int) -> list:
    """木構造のオイラーツアーを行い,通った辺を記録し、木をlistに変換"""
    v = root
    visited = [False for i in range(len(G))]
    ret = []
    node = [root]
    ret, node = dfs(v, visited, ret, node)

    # 各頂点に最初に到達、最後に到達する時間を記録
    in_list = [-1 for i in range(len(G) - 1)]
    out_list = [-1 for i in range(len(G) - 1)]
    for i in range(len(node)):
        if in_list[node[i] - 1] < 0:
            in_list[node[i] - 1] = i
    for i in range(len(node) - 1, -1, -1):
        if out_list[node[i] - 1] < 0:
            out_list[node[i] - 1] = i

    return in_list, out_list, ret, node


print(Euler_tour(1))
