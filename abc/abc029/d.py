s = input()
n = len(s)

dp = [[0] * 2 for _ in range(n + 1)]
# dp[i][smaller] :=
#  * (smaller = 0) 上からi桁がsと完全一致してる時に1を書いた数
#  * (smaller = 1) 上からi桁がsより小さい範囲で1を書いた数

for i in range(n):
    si = ord(s[i]) - ord('0')

    if si == 1:
        dp[i + 1][0] = dp[i][0] + 1
    else:
        dp[i + 1][0] = dp[i][0]

    m = int(s[:i]) if i > 0 else 0
    if si > 1:
        dp[i + 1][1] += dp[i][0] * si  # ... *
        dp[i + 1][1] += 1  #             ... 1
        dp[i + 1][1] += dp[i][1] * 10  # *** *
        dp[i + 1][1] += m  #             *** 1
    else:
        dp[i + 1][1] += dp[i][0] * si  # ... *
        dp[i + 1][1] += dp[i][1] * 10  # *** *
        dp[i + 1][1] += m  #            *** 1

ans = dp[n][0] + dp[n][1]
print(ans)
