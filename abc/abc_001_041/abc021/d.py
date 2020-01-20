def comb(n, k, MOD):
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


MOD = 10**9 + 7
n = int(input())
k = int(input())

ans = comb(n + k - 1, n - 1, MOD)
print(ans)
