n, m = map(int, input().split())
f = [int(input()) for _ in range(n)]

# dp[i] = (ある日までにiまでのサプリを食べる場合の数)
dp = [0] * (n + 1)
dp[0] = 1

s = set()
j = 0
for i in range(n):
    print(i, s)
    while j < n and f[j] not in s:
        s.add(f[j])
        j += 1
        dp[j] += dp[i]
    s.remove(f[i])

print(dp)
print(dp[n])
