from operator import itemgetter
n, p = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=itemgetter(0), reverse=True)

P_MAX = p + 100
dp = [[0] * (P_MAX + 1) for _ in range(n + 1)]
# dp[i][j] = i番目まで見て、合計金額がj円となる
for i, (a_i, b_i) in enumerate(ab):
    for j in range(P_MAX + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j <= p:
            dp[i + 1][j + a_i] = max(dp[i][j + a_i], dp[i][j] + b_i)

# print(*dp, sep='\n')
ans = max(dp[n][p:])
print(ans)
