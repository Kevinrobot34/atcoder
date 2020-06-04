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


MOD = 10**9 + 7
n, k = map(int, input().split())

if k >= n:
    ans = comb(n, k % n, MOD)
else:
    ans = comb(n - 1 + k, k, MOD)
print(ans)
