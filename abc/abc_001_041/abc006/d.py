from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
INF = float('inf')
n = int(input())
c = [int(input()) for _ in range(n)]

dp = [INF] * n
# dp[i] = (長さi+1の増加部分列の最終項のmin)
for i in range(n):
    idx = bisect_left(dp, c[i])
    dp[idx] = c[i]

lis = bisect_left(dp, INF)
ans = n - lis
print(ans)
