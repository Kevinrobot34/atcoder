n, k = map(int, input().split())

MOD = 10**9 + 7
MAX = n + 10
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
for i in range(k, n + 2):
    ans += n * i - i * (i - 1) + 1
    # print(i,
    # i * (i - 1) // 2, n * i - i * (i - 1) // 2, n * i - i * (i - 1) + 1)
    ans %= MOD

print(ans)
