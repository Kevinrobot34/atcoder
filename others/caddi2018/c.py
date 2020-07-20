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


n, p = map(int, input().split())
fact = factorize(p)
ans = 1
for k, v in fact.items():
    ans *= k**(v // n)
print(ans)
