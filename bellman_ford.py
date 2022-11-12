def bellman_ford(G, num_node):
    """ベルマンフォード法
    計算量(VE)に注意"""

    INF = 10**15
    node = [INF for i in range(num_node + 1)]  # スタート地点以外の値は∞で初期化
    node[1] = 0  # スタートの始点は0で初期化

    # 始点から順に辺を探索
    for i in range(num_node):
        update = False
        for start in range(1, num_node + 1):
            for goal, cost in G[start]:
                # 更新条件
                if node[start] + cost < node[goal]:
                    node[goal] = node[start] + cost  # 更新
                    update = True
        # 更新が一度も行わなければ終了
        if not update:
            break
        if i == num_node - 1:
            # 負閉路が存在して正しい解が求められない
            return -1
    return node
