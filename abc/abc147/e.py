h, w = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(h)]
b = [tuple(map(int, input().split())) for _ in range(h)]
c = [[a[i][j] - b[i][j] for j in range(w)] for i in range(h)]

INF = 10**10
dp = [[INF] * (w + 1) for _ in range(h + 1)]
dp[0][0] = c[0][0]
for i in range(h):
    for j in range(w):
        if i < h - 1:
            dp[i + 1][j] = min(
                abs(dp[i + 1][j]),
                abs(c[i + 1][j] + dp[i][j]),
                abs(c[i + 1][j] - dp[i][j]),
            )
        if j < w - 1:
            dp[i][j + 1] = min(
                abs(dp[i][j + 1]),
                abs(c[i][j + 1] + dp[i][j]),
                abs(c[i][j + 1] - dp[i][j]),
            )
        # dp[i][j] = min(abs(c[i][j] + dp[i - 1][j]),
        #                abs(c[i][j] - dp[i - 1][j]),
        #                abs(c[i][j] + dp[i][j - 1]),
        #                abs(c[i][j] - dp[i][j - 1]))

print(*dp, sep='\n')
print(dp[h - 1][w - 1])
