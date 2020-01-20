n, ma, mb = map(int, input().split())
med = [tuple(map(int, input().split())) for _ in range(n)]

INF = 10**8
MAX_M = 400
dp = [[[INF] * (MAX_M + 1) for _ in range(MAX_M + 1)] for _ in range(2)]
dp[0][0][0] = 0
for i, (a, b, c) in enumerate(med):
    i0 = (i + 0) % 2
    i1 = (i + 1) % 2
    for x in range(MAX_M + 1):
        for y in range(MAX_M + 1):
            if x - a >= 0 and y - b >= 0:
                dp[i1][x][y] = min(dp[i0][x][y], dp[i0][x - a][y - b] + c)
            else:
                dp[i1][x][y] = dp[i0][x][y]

ans = INF
for i in range(1, MAX_M + 1):
    if ma * i > MAX_M or mb * i > MAX_M:
        break
    ans = min(ans, dp[n % 2][ma * i][mb * i])
if ans == INF:
    ans = -1

print(ans)
