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


MOD = 1777777777
n, k = map(int, input().split())

c1 = comb(n, k, MOD)

dp = [0] * (k + 1)
dp[2] = 1
for i in range(3, k + 1):
    dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD
c2 = dp[k]

ans = c1 * c2 % MOD
print(ans)
