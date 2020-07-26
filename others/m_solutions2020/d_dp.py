n = int(input())
a = [-1] + list(map(int, input().split()))

# dp[i] = (i+1)日目終了時点での金額の最大値
# dp[i] = max(dp[i-1], {dp[j-1] % a[j] + (dp[j-1] // a[j]) * a[i] | j<i})
dp = [0] * (n + 1)
dp[0] = dp[1] = 1000
dp[2] = max(dp[0] % a[1] + (dp[0] // a[1]) * a[2], dp[1])

for i in range(1, n + 1):
    cand = dp[i - 1]
    for j in range(1, i):
        cand = max(cand, dp[j - 1] % a[j] + (dp[j - 1] // a[j]) * a[i])
    dp[i] = cand

print(dp[n])
