from bisect import bisect_left, bisect_right
n = int(input())
w = [int(input()) for _ in range(n)]

INF = 10**8
dp = [INF] * n
for i in range(n):
    idx = bisect_left(dp, w[i])
    dp[idx] = w[i]

ans = bisect_left(dp, INF)
print(ans)
