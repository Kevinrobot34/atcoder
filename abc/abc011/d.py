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


n, d = map(int, input().split())
x, y = map(int, input().split())

if x % d == 0 and y % d == 0:
    nx = x // d
    ny = y // d
    if nx + ny > n or (n - (nx + ny)) % 2 != 0:
        ans = 0.0
    else:
        pass
else:
    ans = 0.0

print(ans)
