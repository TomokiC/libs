# ビット全探索
# データ数
N = 5
S = [i + 1 for i in range(N)]

# ビット全探索
max_num = 2**N - 1
Answer = 0
for i in range(1, max_num + 1):
    bin_i = list(bin(i)[2:])
    select = []
    for j in range(len(bin_i) - 1, -1, -1):
        if bin_i[j] == "1":
            select.append(S[len(bin_i) - j - 1])
    # selectにSから選んだケースを格納済み
    print(select)
