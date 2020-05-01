n, s = map(int, input().split())
a = tuple(map(int, input().split()))
MOD = 998244353

# dp = [[0] * (s + 1) for _ in range(n + 1)]
# dp[0][0] = 1
# for i in range(n):  # ここをrange(i, n)にすると、f(i, r)の計算ができる
#     for j in range(s + 1):
#         dp[i + 1][j] += dp[i][j]  # do NOT use a[i]
#         if j + a[i] <= s:
#             dp[i + 1][j + a[i]] += dp[i][j]  # USE a[i]
# # f(1, n) = dp[n][s]
# # f(1, i) = dp[i][s] (i = 1, 2, ..., n)
# print('dp')
# print(*dp, sep='\n')

dp0 = [[0] * (s + 1) for _ in range(n + 1)]
dp1 = [[0] * (s + 1) for _ in range(n + 1)]
dp0[0][0] = 1
ans = 0
for i in range(n):
    for j in range(s + 1):
        # i番目の要素は使わない
        dp0[i + 1][j] += dp0[i][j]
        dp0[i + 1][j] %= MOD
        dp1[i + 1][j] += dp0[i][j] + dp1[i][j]
        dp1[i + 1][j] %= MOD

        if j + a[i] <= s:
            dp1[i + 1][j + a[i]] += dp0[i][j] + dp1[i][j]
            dp1[i + 1][j + a[i]] %= MOD

    ans += dp1[i + 1][s]
    ans %= MOD
# dp[r][s][1] = \sum_{i=1}^{r} f(i, r)

# print('dp[][][1]')
# for i in range(n + 1):
#     print([dp[i][j][1] for j in range(s + 1)])

print(ans)
