h, n = map(int, input().split())
magic = [tuple(map(int, input().split())) for _ in range(n)]

INF = 10**10
dp = [INF] * (h + 1)
dp[h] = 0
for i in reversed(range(h + 1)):
    for aj, bj in magic:
        dp[max(0, i - aj)] = min(dp[max(0, i - aj)], dp[i] + bj)

print(dp[0])
