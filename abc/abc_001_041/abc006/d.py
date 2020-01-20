from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
n = int(input())
c = [int(input()) for _ in range(n)]

dp = [c[0]]
for i in range(1, n):
    if dp[-1] < c[i]:
        dp.append(c[i])
    else:
        idx = bisect_left(dp, c[i])
        dp[idx] = c[i]

print(len(c) - len(dp))
