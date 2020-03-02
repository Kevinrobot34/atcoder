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

a_fac = []
lcm_fac = defaultdict(int)
for i in range(n):
    a_fac.append(factorize(a[i]))
    for k, v in a_fac[i].items():
        lcm_fac[k] = max(lcm_fac[k], v)

# print(lcm_fac)
ans = 0
for i in range(n):
    b_i = 1
    for k, v in lcm_fac.items():
        b_i *= pow(k, v - a_fac[i][k], MOD)
        b_i %= MOD
    # print(i, a[i], b_i)
    ans += b_i
    ans %= MOD

print(ans)
