from collections import defaultdict
MOD = 10**9 + 7
n, m = map(int, input().split())
f = [int(input()) for _ in range(n)]

# dp[i] = (ある日までにiまでのサプリを食べる場合の数)
dp = [0] * (n + 1)
dp[0] = 1
dp_cs = [0] * (n + 2)
dp_cs[1] = 1

left = [0] * (n + 1)
f_dict = defaultdict(int)
l = 0
for r in range(n):
    f_dict[f[r]] += 1
    while l < r and f_dict[f[r]] > 1:
        f_dict[f[l]] -= 1
        l += 1
    left[r + 1] = l

for i in range(1, n + 1):
    dp[i] = dp_cs[i] - dp_cs[left[i]] + MOD
    dp[i] %= MOD
    dp_cs[i + 1] = dp_cs[i] + dp[i]
    dp_cs[i + 1] %= MOD

ans = dp[n]
# print(left)
# print(dp)
# print(dp_cs)
print(ans)
