import sys
input = sys.stdin.readline

n, t = map(int, input().split())
dish = [tuple(map(int, input().split())) for _ in range(n)]
# dish.sort()
# print(*dish, sep='\n')

dp = [[0] * (t + 1) for _ in range(n + 1)]
for i in range(n):
    for t0 in range(t):
        dp[i + 1][t0] = dp[i][t0]
    for t0 in range(t):
        t1 = min(t0 + dish[i][0], t)
        dp[i + 1][t1] = max(dp[i + 1][t1], dp[i][t1], dp[i][t0] + dish[i][1])

ans = max(dp[n])
# print(*dp, sep='\n')
print([dp[i][-1] for i in range(n + 1)])
print(dp[-3:])
print(ans)
