n = int(input())
a = list(map(int, input().split()))
a2 = [(a[i], i) for i in range(n)]
a2.sort(reverse=True)
# print(a2)

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i, (aj, j) in enumerate(a2):
    for k in range(i + 1):
        # left
        dp[i + 1][k + 1] = max(dp[i][k] + aj * abs(k - j), dp[i + 1][k + 1])

        # right
        dp[i + 1][k] = max(dp[i][k] + aj * abs((n - i + k - 1) - j),
                           dp[i + 1][k])

ans = max(dp[n])
print(ans)
# print(*dp, sep='\n')
