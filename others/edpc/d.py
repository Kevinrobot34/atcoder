import sys
input = sys.stdin.readline

n, w = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i, (wi, vi) in enumerate(items):
    for j in range(w + 1):
        if j >= wi:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - wi] + vi)
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[n][w])
