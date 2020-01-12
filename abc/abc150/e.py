MOD = 10**9 + 7
n = int(input())
c = list(map(int, input().split()))
c.sort()

if n > 1:
    ans = 0
    x = (1 << (n - 1)) % MOD
    y = (1 << (n - 2)) % MOD
    for i in range(n):
        m = x + (y * (n - 1 - i)) % MOD
        m %= MOD
        ans += c[i] * m
        ans %= MOD

    for i in range(n):
        ans *= 2
        ans %= MOD
else:
    ans = c[0] * 2
    ans %= MOD
print(ans)
