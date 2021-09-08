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


n = int(input())
if n > 1:
    f = factorize(n)

    MAX = max(f.values())
    b = [0]
    while len(b) < MAX + 10:
        b.extend([b[-1] + 1] * (b[-1] + 2))

    # print(b)
    # print(f)
    ans = 0
    for v in f.values():
        ans += b[v]
else:
    ans = 0

print(ans)
