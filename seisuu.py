import math


# 最大公約数を計算
def saidai_kouyakusuu(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a > 0:
        return a
    else:
        return b


# 最小公倍数を計算
def saishou_koubaisuu(a, b):
    G = saidai_kouyakusuu(a, b)
    return a * b / G


def yakusuu_rekkyo(a: int) -> list:
    """aの約数を全列挙 O(√N)"""
    max_num = int(math.sqrt(a))
    answer = []
    for i in range(1, max_num + 1):
        if a % i == 0:
            if i != a // i:
                answer.append(i)
                answer.append(a // i)
            else:
                answer.append(i)
    answer.sort()
    return answer
