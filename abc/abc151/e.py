MOD = 10**9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

MAX = 10**5 + 100
fact = [1] * (MAX + 1)  # i!
finv = [1] * (MAX + 1)  # (i!)^{-1}
iinv = [1] * (MAX + 1)  # i^{-1}
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD


def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n - k] % MOD


ans = 0
for i in range(n):
    # min
    ans -= a[i] * comb(n - 1 - i, k - 1)
    ans %= MOD
    # max
    ans += a[i] * comb(i, k - 1)
    ans %= MOD
    # print(comb(n - 1 - i, k - 1), comb(i, k - 1))

print(ans)
