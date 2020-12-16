n = int(input())
p = list(map(float, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
# dp[i][j] = (コインiまで見て、表がj枚出ている確率)

dp[1][0] = 1 - p[0]
dp[1][1] = p[0]

for i in range(1, n):
    for j in range(i + 2):
        if j == 0:
            dp[i + 1][j] = (1 - p[i]) * dp[i][j]
        else:
            dp[i + 1][j] = p[i] * dp[i][j - 1] + (1 - p[i]) * dp[i][j]

ans = sum(dp[n][(n + 1) // 2:])
# print(*dp, sep='\n')
print(ans)
