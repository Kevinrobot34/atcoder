MOD = 10**9 + 7
h, w = map(int, input().split())
a = [input() + '#' for _ in range(h)]
a.append('#' * (w + 1))

dp = [[0] * (w + 1) for _ in range(h + 1)]

dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            continue
        if a[i + 1][j] == '.':
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
        if a[i][j + 1] == '.':
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= MOD

ans = dp[h - 1][w - 1]
print(ans)
