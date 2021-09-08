MOD = 998244353
n, m, k = map(int, input().split())

MAX = 2 * 10**5 + 5
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


mm = [1]
for j in range(n):
    mm.append((mm[-1] * (m - 1)) % MOD)
# print(mm)
dp = [(comb(n - 1, j) * m * mm[n - 1 - j]) % MOD for j in range(k + 1)]
# print(dp)

ans = sum(dp) % MOD
print(ans)
