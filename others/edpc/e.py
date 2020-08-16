import sys
input = sys.stdin.readline

n, w = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

V_MAX = 10**5
dp = [[w + 1] * (V_MAX + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i, (wi, vi) in enumerate(items):
    for j in range(V_MAX + 1):
        if j >= vi:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - vi] + wi)
        else:
            dp[i + 1][j] = dp[i][j]

ans = 0
for j in range(V_MAX + 1):
    if dp[n][j] <= w:
        ans = max(ans, j)

print(ans)
