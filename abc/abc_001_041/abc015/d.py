import sys
input = sys.stdin.readline

W = int(input())
n, K = map(int, input().split())
ss = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[[0] * (W + 1) for _ in range(K + 1)] for _ in range(n + 1)]

for i, (ai, bi) in enumerate(ss):
    for k in range(K + 1):
        for w in range(W + 1):
            dp[i + 1][k][w] = dp[i][k][w]
    for k in range(min(i + 1, K)):
        for w in range(W):
            if w + ai <= W:
                dp[i + 1][k + 1][w + ai] = max(dp[i + 1][k + 1][w + ai],
                                               dp[i][k][w] + bi)
    # print(*dp[i], sep='\n')
    # print(i)

ans = 0
for k in range(K + 1):
    ans = max(ans, max(dp[n][k]))
# print(*dp[n], sep='\n')
print(ans)
