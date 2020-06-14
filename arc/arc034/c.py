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
a, b = map(int, input().split())
fact = defaultdict(int)
for x in range(b + 1, a + 1):
    fact_x = factorize(x)
    for k, v in fact_x.items():
        fact[k] += v

ans = 1
for v in fact.values():
    ans *= v + 1
    ans %= MOD

print(ans)
