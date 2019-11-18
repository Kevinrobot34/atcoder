MOD = 10**9 + 7


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


x, y = map(int, input().split())
a = 2 * y - x
b = 2 * x - y

if a < 0 or b < 0:
    ans = 0
elif a % 3 != 0 or b % 3 != 0:
    ans = 0
else:
    a //= 3
    b //= 3
    # print(a, b)
    ans = comb(a + b, a, MOD)

print(ans)
