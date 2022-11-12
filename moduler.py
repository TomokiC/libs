import math


# 累乗の余り
def calc_ruijou_amari(a, b, M):
    """a^bをMで割った余りを計算O(log(b))"""
    # a^bをMで割ったあまりを計算
    # 繰り返し二乗方を使う
    exponent = b
    # 2進数変換
    bin_expo = list(map(int, list(str(bin(exponent))[2:])))
    bin_expo = bin_expo[::-1]
    # a^1,a^2,a^4,..を計算
    length = len(bin_expo)
    A = [0 for i in range(length)]
    A[0] = a
    for i in range(1, length):
        A[i] = A[i - 1] ** 2
        A[i] = A[i] % M
    # あまりを掛け算して計算
    Answer = 1
    for i in range(length):
        if bin_expo[i] == 1:
            Answer *= A[i]
            Answer = Answer % M
    return Answer


# モヂュラー逆数
def modinv(a, b, M):
    """a/bをMで割ったあまり計算O(log(b)) ※Mは素数でないといけない"""

    # b^(M-2)をMで割ったあまりを計算（モデュラー逆数）
    moduler_g = pow(b, M - 2, M)

    return (a * moduler_g) % M


def factorial_amari(a, M) -> int:
    """a!をMで割ったあまりを計算O(a)"""
    if M == 1:
        return int(math.factorial(a))
    answer = 1
    for i in range(1, a + 1):
        answer *= i % M
        answer = answer % M
    return answer


def calc_combination(a, b, M) -> int:
    """aCbを計算し,Mで割ったあまりを計算(O(a))"""
    if M == 1:
        return int(math.factorial(a) / math.factorial(b) / math.factorial(a - b))
    tmp_u = factorial_amari(a, M)
    tmp_d = ((factorial_amari(b, M)) * (factorial_amari(a - b, M))) % M
    return moduler(tmp_u, tmp_d, M)


print(calc_ruijou_amari(3, 11, 11))
print((3**11) % 11)
