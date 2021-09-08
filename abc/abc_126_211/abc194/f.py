MOD = 10**9 + 7
base = 16
n, k = input().split()
k = int(k)
l = len(n)

dp1 = [[0] * (base + 2) for _ in range(l + 1)]
dp2 = [[0] * (base + 2) for _ in range(l + 1)]
# dp1[i][j] : (16進数で)上から i 桁はnと一致していて、使われている数字がj種類であるような数
# dp2[i][j] : (16進数で)上から i 桁が既にnより小さく、使われている数字がj種類であるような数

dp1[0][0] = 1
digit_set = set()
for i in range(l):
    ni = int(n[i], base)
    j = len(digit_set)

    # 1 -> 1
    j_11 = len(digit_set | {ni})
    dp1[i + 1][j_11] += dp1[i][j]
    dp1[i + 1][j_11] %= MOD

    # 1 -> 2
    for x in range(ni):
        if j == 0 and x == 0:
            # Leading zero用の処理
            dp2[i + 1][0] += dp1[i][0]
            dp2[i + 1][0] %= MOD
        else:
            j_12 = j if x in digit_set else j + 1
            dp2[i + 1][j_12] += dp1[i][j]
            dp2[i + 1][j_12] %= MOD

    # 2 -> 2
    for x in range(base + 1):
        if x == 0:
            # Leading zero用の処理
            dp2[i + 1][x] += dp2[i][x]
            dp2[i + 1][x + 1] += dp2[i][x] * (base - 1)
        else:
            dp2[i + 1][x] += dp2[i][x] * x
            dp2[i + 1][x + 1] += dp2[i][x] * (base - x)

        dp2[i + 1][x] %= MOD
        dp2[i + 1][x + 1] %= MOD

    digit_set.add(ni)

ans = (dp1[l][k] + dp2[l][k]) % MOD
print(ans)
