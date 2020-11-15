MOD = 10**9 + 7
h, w = map(int, input().split())
s = ['#' * (w + 2)]
s += ['#' + input() + '#' for _ in range(h)]
s += ['#' * (w + 2)]

dp = [[0] * (w + 2) for _ in range(h + 2)]
dp_cs1 = [[0] * (w + 2) for _ in range(h + 2)]
dp_cs2 = [[0] * (w + 2) for _ in range(h + 2)]
dp_cs3 = [[0] * (w + 2) for _ in range(h + 2)]
dp[1][1] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '#':
            continue

        dp[i][j] += dp_cs1[i - 1][j] + dp_cs2[i][j - 1] + dp_cs3[i - 1][j - 1]
        dp[i][j] %= MOD
        dp_cs1[i][j] = (dp_cs1[i - 1][j] + dp[i][j]) % MOD
        dp_cs2[i][j] = (dp_cs2[i][j - 1] + dp[i][j]) % MOD
        dp_cs3[i][j] = (dp_cs3[i - 1][j - 1] + dp[i][j]) % MOD

# print(*dp_cs1, sep='\n')
# print()
# print(*dp_cs2, sep='\n')
# print()
# print(*dp_cs3, sep='\n')
# print()
# print(*dp, sep='\n')
print(dp[h][w])
