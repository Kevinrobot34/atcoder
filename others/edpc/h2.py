MOD = 10**9 + 7
h, w = map(int, input().split())
a = ['#' * (w + 1)] + ['#' + input() for _ in range(h)]

dp = [[0] * (w + 1) for _ in range(h + 1)]

dp[0][1] = 1
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if a[i][j] == '#':
            continue
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

print(dp[h][w])
