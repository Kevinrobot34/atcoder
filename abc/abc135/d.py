s = input()
MOD = 10**9 + 7

dp = [[0 for i in range(13)] for j in range(2)]
if s[0] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(s[0])] = 1

for i in range(1, len(s)):
    for j in range(13):
        dp[i%2][j] = 0

    if s[i] == '?':
        for j in range(13):
            for k in range(10):
                dp[i%2][(10*j+k)%13] = (dp[i%2][(10*j+k)%13] + dp[(i-1)%2][j]) % MOD
    else:
        k = int(s[i])
        for j in range(13):
            dp[i%2][(10*j+k)%13] = (dp[i%2][(10*j+k)%13] + dp[(i-1)%2][j]) % MOD

    # print(dp[(i-1)%2])
    # print(dp[i%2])
    # print()


print(dp[(len(s)-1)%2][5])
