def GCD(a:int , b: int) -> int:
    return a if b == 0 else GCD(b, a % b)

from collections import defaultdict
def factorize(n: int) -> dict:
    f = defaultdict(int)
    p = 2
    while n > 1:
        while n % p == 0:
            f[p] += 1
            n = n // p
        p += 1 if p == 2 else 2
    return f

a, b = map(int, input().split())
factors = factorize(GCD(a, b))

ans = len(fa0)

print(ans)
