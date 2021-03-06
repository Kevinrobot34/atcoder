MOD = 10**9 + 7
base = 10
d = int(input())
k = input()
n = len(k)
dp1 = [[0] * d for _ in range(n + 1)]
dp2 = [[0] * d for _ in range(n + 1)]
# dp1[i][j] : 上からi桁はkと一致していて、そこまでの各桁の数字の和をdで割った余りがj
# dp2[i][j] : 上からi桁が既にnより小さく、そこまでの各桁の数字の和をdで割った余りがj

dp1[0][0] = 1
x = 0
for i in range(n):
    ki = int(k[i])
    # 1 -> 1
    j_11 = (x + ki) % d
    dp1[i + 1][j_11] += dp1[i][x]
    dp1[i + 1][j_11] %= MOD

    # 1 -> 2
    for a in range(ki):
        j_12 = (x + a) % d
        dp2[i + 1][j_12] += dp1[i][x]
        dp2[i + 1][j_12] %= MOD

    # 2 -> 2
    for y in range(d):
        for a in range(base):
            j_22 = (y + a) % d
            dp2[i + 1][j_22] += dp2[i][y]
            dp2[i + 1][j_22] %= MOD

    x = (x + ki) % d

ans = (dp1[n][0] + dp2[n][0] - 1) % MOD  # 0は取り除く
print(ans)
