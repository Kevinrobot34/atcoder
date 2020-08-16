n = int(input())
h = tuple(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0
dp[1] = abs(h[0] - h[1])
# dp[i] = (足場iにたどり着いた時点でのコストの最小値)

for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[n - 1])
