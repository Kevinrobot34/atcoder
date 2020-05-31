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
            dp[i + 1][j] = dp[i][j] + dp[i][j - ai]
        else:
            dp[i + 1][j] = dp[i][j]

print(*dp, sep='\n')
print(dp[n][s])
# # dp[i][j] = i個使って和がjとなるような場合の数
# dp = [[defaultdict(int)] * (s + 1) for _ in range(n + 1)]
# dp[0][0][0] = 1
# for ai in a:
#     dp[1][ai] += 1
