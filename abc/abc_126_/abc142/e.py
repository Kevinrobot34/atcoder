import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# INF = float("inf")
INF = 10 ** 8
dp = [INF] * ((1<<n) + 1)
dp[0] = 0

for i in range(m):
    a, b = map(int, input().split())
    c = sum(1<<(ci-1) for ci in map(int, input().split()))

    for j in range(1<<n):
        if dp[j] + a < dp[j | c]:
            dp[j | c] = dp[j] + a
        # dp[j | c] = min(dp[j] + a, dp[j | c])


if dp[(1<<n) - 1] == INF:
    ans = -1
else:
    ans = dp[(1<<n) - 1]

print(ans)
