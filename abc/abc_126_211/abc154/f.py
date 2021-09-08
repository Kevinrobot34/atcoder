r1, c1, r2, c2 = map(int, input().split())

MOD = 10**9 + 7
MAX = r2 + c2 + 10
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


def func(a, b):
    res = 0
    for i in range(a + 1):
        res += comb(i + b + 1, i + 1)
        res %= MOD
    return res


ans = func(r2, c2) - func(r2, c1 - 1) - func(r1 - 1, c2) + func(r1 - 1, c1 - 1)
ans %= MOD
print(ans)
