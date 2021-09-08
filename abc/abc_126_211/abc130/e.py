MOD = 10**9 + 7
n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
cs = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = 1 + cs[i-1][j-1]
            dp[i][j] %= MOD

        cs[i][j] = cs[i-1][j] + cs[i][j-1] - cs[i-1][j-1] + dp[i][j]
        cs[i][j] %= MOD

print((cs[n][m] + 1) % MOD)
