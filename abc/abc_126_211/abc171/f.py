MOD = 10**9 + 7
k = int(input())
s = input()
n = len(s)

MAX = 2 * 10**6 + 5
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
for i in range(k + 1):
    ans += comb(n + k - i - 1, k - i) * pow(25, k - i, MOD) % MOD * pow(
        26, i, MOD) % MOD
    ans %= MOD

print(ans)
