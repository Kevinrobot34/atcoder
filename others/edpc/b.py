n, k = map(int, input().split())
h = tuple(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0
# dp[i] = (足場iにたどり着いた時点でのコストの最小値)

for i in range(n):
    for j in range(i + 1, min(i + k + 1, n)):
        dp[j] = min(dp[j], dp[i] + abs(h[j] - h[i]))

print(dp[n - 1])
