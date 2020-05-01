MOD = 10**9 + 7
n, m = map(int, input().split())
f = [int(input()) for _ in range(n)]

# dp[i] = (ある日までにiまでのサプリを食べる場合の数)
dp = [0] * (n + 1)
dp[0] = 1
dp_cs = [0] * (n + 1)

left = 0
s = set()
for i in range(n):
    dp_cs[i + 1] = dp_cs[i] + dp[i]
    dp_cs[i + 1] %= MOD

    if f[i] not in s:
        s.add(f[i])
    else:
        #s.remove(f[i])
        while f[left] != f[i]:
            left += 1
        left += 1

    # for j in range(left, i + 1):
    #     dp[i + 1] += dp[j]
    dp[i + 1] = dp_cs[i + 1] - dp_cs[left] + MOD
    dp[i + 1] %= MOD
    # print(i, left)

print(dp[n])
