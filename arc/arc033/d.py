MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
t = int(input())

fact = [1] * (n + 1)  # i!
finv = [1] * (n + 1)  # (i!)^{-1}
iinv = [1] * (n + 1)  # i^{-1}
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD

b = [1] * (n + 1)
for i in range(n + 1):
    b[i] = ((-1)**(n - i) * a[i] * finv[i] * finv[n - i]) % MOD

x = 1
for i in range(n + 1):
    x *= t - i
    x %= MOD

ans = 0
for i in range(n + 1):
    ans += b[i] * x * pow(t - i, MOD - 2, MOD) % MOD
    ans %= MOD

print(ans)
