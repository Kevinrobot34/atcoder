from bisect import bisect_left, bisect_right
MOD = 10**9 + 7

n, k = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * k for _ in range(n)]
dp[0] = [1] * k

for i in range(1, n):
    cs = [0] * (k + 1)
    for j in range(k):
        cs[j + 1] = cs[j] + dp[i - 1][j]
        cs[j + 1] %= MOD

    for j in range(k):
        idx = bisect_right(v[i - 1], v[i][j])
        dp[i][j] = cs[idx]

ans = sum(dp[-1]) % MOD
print(ans)
