# 二分探索

# サンプル用リスト
a = [1, 2, 3, 5]
# ある条件を貸した時にTrue,Falseを返す
def isOK(index, key):
    # 条件
    if a[index] >= key:
        return True
    else:
        return False


def binary_serch_():
    """key:keyを与えた時に条件を満たす最小のインデックスを出力
    探索幅を半分にしながら差が１になるまで探索する"""
    # 端の初期地はカスタムする
    # 最小値-1
    left = -1
    # 最大値+1
    right = 10**18
    mergin = 1

    # 以下はカスタムしない
    while right - left > mergin:
        mid = (left + right) // 2

        if isOK(mid):
            left = mid
        else:
            right = mid

    # ここでrightは条件を満たさない最小のインデックス
    # leftは条件を満たす最大のインデックスになる
    return left
