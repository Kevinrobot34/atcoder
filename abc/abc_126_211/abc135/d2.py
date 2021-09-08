MOD = 10**9 + 7
s = input()
n = len(s)

# dp[i][r] = (最初のi桁を見て、余りがrとなるような個数)
dp = [[0] * 13 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    if s[i] == '?':
        for r in range(13):
            for d in range(10):
                r1 = (r * 10 + d) % 13
                dp[i + 1][r1] += dp[i][r]
                dp[i + 1][r1] %= MOD
    else:
        for r in range(13):
            r1 = (r * 10 + int(s[i])) % 13
            dp[i + 1][r1] += dp[i][r]
            dp[i + 1][r1] %= MOD

ans = dp[n][5]
# print(*dp, sep='\n')
print(ans)
