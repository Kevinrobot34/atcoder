from collections import defaultdict
import sys
input = sys.stdin.readline

n, w = map(int, input().split())
obj = [list(map(int, input().split())) for _ in range(n)]

dp = [defaultdict(int), defaultdict(int)]
dp[0][0] = 0
for i in range(n):
    wi, vi = obj[i]
    # print(dp[i%2])
    dp[(i+1)%2] = dp[i%2].copy()
    for w0 in dp[i%2]:
        # dp[(i+1)%2][w0] = dp[i%2][w0]
        if w0 + wi <= w:
            dp[(i+1)%2][w0 + wi] = max(dp[(i+1)%2][w0 + wi], dp[i%2][w0] + vi)

# print(dp[n%2])
print(max(dp[n%2].values()))
