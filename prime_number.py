import math
import time


def calc_prime(n: int) -> list:
    """n以下の素数を全羅列(n>=2) O(N)"""
    if n < 2:
        return []
    A = [False for i in range(n + 1)]
    Answer = []
    A[0] = True
    A[1] = True
    prime_num = 2
    while prime_num <= int(math.sqrt(n)):
        for j in range(2, n // prime_num + 1):
            A[prime_num * j] = True
        for k in range(prime_num + 1, n + 1):
            if not A[k]:
                prime_num = k
                break

    for i in range(2, n + 1):
        if not A[i]:
            Answer.append(i)
    return Answer


def isprime(a: int) -> bool:
    """素数かどうか判定O(√N)"""
    if a == 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


N = 10000000
st = time.time()
print(len(calc_prime(N)))
print(time.time() - st)

# ct = 0
# st = time.time()
# for i in range(1, N + 1):
#     if isprime(i):
#         ct += 1
# print(ct)
# print(time.time() - st)
