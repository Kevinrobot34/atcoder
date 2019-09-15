from collections import defaultdict
n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [defaultdict(int) for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in reversed(range(n)):
        for s in dp[j]:
            dp[j+1][s+x[i]] += dp[j][s]

# for dp_i  in dp:
#     print(dp_i)

ans = 0
for i in range(1, len(dp)):
    ans += dp[i][a*i]
print(ans)
