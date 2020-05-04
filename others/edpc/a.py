n = int(input())
h = tuple(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0
# dp[i] = (足場iにたどり着いた時点でのコストの最小値)

for i in range(n):
    if i + 1 < n:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))

print(dp[n - 1])
