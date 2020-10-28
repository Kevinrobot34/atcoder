INF = 10**10
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

cost = [[0] * n for _ in range(n)]
for i, (xi, yi, zi) in enumerate(cities):
    for j, (xj, yj, zj) in enumerate(cities):
        cost[i][j] = abs(xj - xi) + abs(yj - yi) + max(0, zj - zi)
dp = [[INF] * n for _ in range(1 << n)]
dp[0][0] = 0

for bit in range(1 << n):
    for i in range(n):
        for j in range(n):
            nbit = bit | (1 << j)
            dp[nbit][j] = min(dp[nbit][j], dp[bit][i] + cost[i][j])

print(dp[(1 << n) - 1][0])
