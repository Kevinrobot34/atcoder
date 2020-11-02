def pow(x: int, y: int, MOD: int) -> int:
    # return (x**y) % MOD with O(log y)
    ret = 1
    while y:
        if y & 1:
            ret = ret * x % MOD
        x = (x**2) % MOD
        y = y // 2
    return ret


MOD = 998244353
n, k = map(int, input().split())
a = list(map(int, input().split()))

fact = [1] * (k + 1)  # i!
finv = [1] * (k + 1)  # (i!)^{-1}
iinv = [1] * (k + 1)  # i^{-1}
for i in range(2, k + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD

memo = [0] * (k + 1)
for x in range(k + 1):
    val = sum(pow(ai, x, MOD) for ai in a) * finv[x] % MOD
    memo[x] = val

sub = [0] * (k + 1)
for x in range(k + 1):
    sub[x] = sum(pow(2 * ai, x, MOD) for ai in a) % MOD

inv2 = pow(2, MOD - 2, MOD)
for x in range(1, k + 1):
    val = fact[x] * sum(memo[i] * memo[x - i] % MOD
                        for i in range(x + 1)) % MOD
    ans = (val - sub[x]) % MOD * inv2 % MOD
    print(ans)
