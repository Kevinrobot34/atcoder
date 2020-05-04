n = int(input())
happy = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n + 1)]
# dp[i][j] = (i日にjをするような場合の幸福度の最大値)

for i in range(n):
    dp[i + 1][0] = max(dp[i][1], dp[i][2]) + happy[i][0]
    dp[i + 1][1] = max(dp[i][2], dp[i][0]) + happy[i][1]
    dp[i + 1][2] = max(dp[i][0], dp[i][1]) + happy[i][2]

ans = max(dp[n])
print(ans)
