n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
# dp[i][j] = (a[:i] と b[:j]までの時の答え)

for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min(
            dp[i - 1][j] + 1,  # a[i-1]は削除
            dp[i][j - 1] + 1,  # b[j-1]は削除
            dp[i - 1][j - 1] +
            int(a[i - 1] != b[j - 1]),  # a[i-1], b[j-1]を末尾に追加
        )

# print(*dp, sep='\n')
print(dp[n][m])
