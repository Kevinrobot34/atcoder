from bisect import bisect_left
INF = 10**8
n = int(input())
a = list(map(int, input().split()))
dp = [INF] * n
# dp[i] = (長さ(i+1)の増加部分列での末尾の項がとりうる最小値)
for ai in a:
    dp[bisect_left(dp, ai)] = ai
print(bisect_left(dp, INF))
