n = int(input())
r = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]
dp[0][0] = dp[0][1] = 1

for i in range(1, n):
    dp[i][0] = max([-1] + [dp[j][1] for j in range(i) if r[i] > r[j]]) + 1
    dp[i][1] = max([-1] + [dp[j][0] for j in range(i) if r[i] < r[j]]) + 1

# print(*dp, sep='\n')
ans = max(dp[n - 1])
if ans < 3:
    ans = 0
print(ans)
