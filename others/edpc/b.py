n, k = map(int, input().split())
h = tuple(map(int, input().split()))

INF = 10**10
dp = [INF] * n
dp[0] = 0
# dp[i] = (足場iにたどり着いた時点でのコストの最小値)

for i in range(1, n):
    dp[i] = min(dp[j] + abs(h[j] - h[i]) for j in range(max(0, i - k), i))

print(dp[n - 1])
