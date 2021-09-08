s = int(input())

MOD = 10**9 + 7
MAX = 2000 + 5
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
for n in range(1, s + 1):
    if s - 3 * n < 0:
        break
    ans += comb((s - 3 * n) + (n - 1), n - 1)
    ans %= MOD

print(ans)
