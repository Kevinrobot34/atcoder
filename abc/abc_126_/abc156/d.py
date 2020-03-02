n, a, b = map(int, input().split())
MOD = 10**9 + 7


def comb(n: int, k: int, MOD: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1
    iinv = [1] * (k + 1)
    ans = n
    for i in range(2, k + 1):
        iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
        ans *= (n + 1 - i) * iinv[i] % MOD
        ans %= MOD
    return ans


# ans = ((1 << n) - 1) % MOD
ans = (pow(2, n, MOD) - 1) % MOD
ans -= comb(n, a, MOD)
ans -= comb(n, b, MOD)
ans %= MOD
print(ans)
