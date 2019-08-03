h, w, k = map(int, input().split())
MOD = 10**9 + 7

dp = [[0]*w for i in range(h+1)]
dp[0][0] = 1

# print(dp[0])
for i in range(1, h+1):
    if w == 1:
        # 線が一本のみの場合
        dp[i][0] = dp[i-1][0]
        continue

    for bits in range(1<<(w-1)):
        if bits & (bits>>1) != 0:
            # 1が隣り合うような場合は適切なあみだくじではない
            continue

        # print(bits, ''.join([str((bits>>j)&1) for j in range(w-1)]))

        for j in range(w-1):
            if (bits>>j) & 1 == 1:
                dp[i][j+1] += dp[i-1][j]
                dp[i][j+1] %= MOD
                dp[i][j] += dp[i-1][j+1]
                dp[i][j] %= MOD
            else:
                if j == 0 or (bits>>(j-1)) & 1 == 0:
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] %= MOD

                if j == w-2:
                    dp[i][w-1] += dp[i-1][w-1]
                    dp[i][w-1] %= MOD
    # print(i, dp[i])

print(dp[h][k-1])
