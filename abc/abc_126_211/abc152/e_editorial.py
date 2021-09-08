from collections import defaultdict


def factorize(n: int) -> dict:
    f = defaultdict(int)
    while n % 2 == 0:
        f[2] += 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            f[p] += 1
            n //= p
        p += 2
    if n != 1:
        f[n] += 1
    return f


MOD = 10**9 + 7
n = int(input())
a = tuple(map(int, input().split()))

MAX_a = max(a)
iinv = [1] * (MAX_a + 1)
for i in range(2, MAX_a + 1):
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD

a_fac = []
lcm_fac = defaultdict(int)
for a_i in a:
    a_fac_i = factorize(a_i)
    a_fac.append(a_fac_i)
    for k, v in a_fac_i.items():
        lcm_fac[k] = max(lcm_fac[k], v)

lcm = 1
for k, v in lcm_fac.items():
    lcm *= pow(k, v, MOD)
    lcm %= MOD

ans = 0
for i in range(n):
    ans += lcm * iinv[a[i]]
    ans %= MOD

print(ans)
