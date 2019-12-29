import sys
input = sys.stdin.readline

h, w = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(h)]
b = [tuple(map(int, input().split())) for _ in range(h)]
c = [[abs(a[i][j] - b[i][j]) for j in range(w)] for i in range(h)]

CONST = 80 * 80 * 2
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1 << (c[0][0] + CONST)

for i in range(h):
    for j in range(w):
        if i < h - 1:
            dp[i + 1][j] |= (dp[i][j] << c[i + 1][j])
            dp[i + 1][j] |= (dp[i][j] >> c[i + 1][j])
        if j < w - 1:
            dp[i][j + 1] |= (dp[i][j] << c[i][j + 1])
            dp[i][j + 1] |= (dp[i][j] >> c[i][j + 1])

for k in range(CONST):
    if dp[h - 1][w - 1] & (1 << (CONST + k)) != 0 or dp[h - 1][w - 1] & (
            1 << (CONST - k)) != 0:
        ans = k
        break

print(ans)
