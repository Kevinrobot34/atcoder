n = int(input())
a = [-1] + list(map(int, input().split()))

# dp[i] = (i+1)日目終了時点での金額の最大値
# dp[i+1] = max(dp[i], {dp[j] % a[k] + (dp[j] // a[k]) * a[l] | j<k<l<=i})
dp = [0] * (n + 1)
dp[0] = dp[1] = 1000
dp[2] = max(dp[0] % a[1] + (dp[0] // a[1]) * a[2], dp[1])

# print(a)
# print(dp)

for i in range(1, n + 1):
    cand = dp[i - 1]
    for j in range(i):
        for k in range(j + 1, i):
            for l in range(k + 1, i + 1):
                cand = max(cand, dp[j] % a[k] + (dp[j] // a[k]) * a[l])
    dp[i] = cand

print(dp[n])
