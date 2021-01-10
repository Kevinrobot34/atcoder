n = int(input())
p = list(map(int, input().split()))

MAX = 10**4
dp = [0] * (MAX + 1)
dp[0] = 1

for i in range(n):
    for j in reversed(range(MAX - p[i] + 1)):
        dp[j + p[i]] += dp[j]

ans = sum(1 for i in range(MAX + 1) if dp[i] > 0)
print(ans)
