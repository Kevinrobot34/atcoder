n, m = map(int, input().split())

MOD = 10**9 + 7
MAX = m + 1
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


def perm(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return fact[n] * finv[n - k] % MOD


ans = perm(m, n)
for i in range(1, n + 1):
    ans += (-1)**(i % 2) * comb(n, i) * perm(m - i, n - i) % MOD
    ans %= MOD

ans *= perm(m, n)
ans %= MOD

print(ans)
