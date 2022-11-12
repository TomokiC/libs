def l_sort(a: list, b: list) -> list:
    """b順に昇順ソートしたaを返す"""
    indx = [i for i in range(len(a))]
    indx.sort(key=lambda x: b[x])
    ret = []
    for i in range(len(indx)):
        ret.append(a[indx[i]])
    return ret


def lexsort(a: list, b: list) -> list:
    """bを基準に昇順ソート、同値の部分に関してはaを基準に昇順ソートしたインデックスを返す
    計算量O(Nlog(N))"""
    indx = [i for i in range(len(a))]

    indx.sort(key=lambda x: b[x])
    a = l_sort(a, b)
    b.sort()

    d = {indx[i]: a[i] for i in range(len(a))}

    indxs = [[indx[0]]]
    for i in range(1, len(b)):
        if b[i] == b[i - 1]:
            indxs[-1].append(indx[i])
        else:
            indxs.append([indx[i]])
    for i in range(len(indxs)):
        indxs[i].sort(key=lambda x: d[x])

    ret = []
    for i in range(len(indxs)):
        ret.extend(indxs[i])
    return ret
