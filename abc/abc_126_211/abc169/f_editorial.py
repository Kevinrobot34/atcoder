from collections import defaultdict
MOD = 998244353
n, s = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] = i番目まで見て和がjとなるような場合の数
dp = [[0] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i, ai in enumerate(a):
    for j in range(s + 1):
        if j - ai >= 0:
            dp[i + 1][j] = (dp[i][j] * 2 + dp[i][j - ai]) % MOD
        else:
            dp[i + 1][j] = dp[i][j] * 2 % MOD

# print(*dp, sep='\n')
print(dp[n][s])
