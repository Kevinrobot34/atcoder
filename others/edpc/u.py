n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# dp[bit] = (集合bitに対する総得点の最大値)
dp = [0] * (1 << n)

# cost[bit] = (集合bitを1つのグループにした際の得点)
cost = [0] * (1 << n)

for bit in range(1 << n):
    for i in range(n):
        if not (bit >> i) & 1:
            continue
        for j in range(i + 1, n):
            if not (bit >> j) & 1:
                continue
            cost[bit] += a[i][j]

for bit in range(1 << n):
    t = bit
    while t > 0:
        dp[bit] = max(dp[bit], dp[bit - t] + cost[t])
        t = (t - 1) & bit

print(dp[(1 << n) - 1])
