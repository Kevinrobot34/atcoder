n, k = map(int, input().split())

MOD = 10**9 + 7
MAX = 2 * n + 1
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


if k >= n - 1:
    ans = comb(n + (n - 1), n - 1)
else:
    ans = 0
    for i in range(k + 1):
        ans += (comb(n, i) * comb(n - 1, i)) % MOD
        ans %= MOD

print(ans)
