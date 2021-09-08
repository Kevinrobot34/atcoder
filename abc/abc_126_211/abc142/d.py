def GCD(a:int , b: int) -> int:
    return a if b == 0 else GCD(b, a % b)

from collections import defaultdict
def factorize(n: int) -> dict:
    f = defaultdict(int)
    tmp_n = n
    p = 2
    while tmp_n > 1 and p * p < n:
        while tmp_n % p == 0:
            f[p] += 1
            tmp_n = tmp_n // p
        p += 1 if p == 2 else 2

    if tmp_n != 1:
        f[tmp_n] += 1
    return f

a, b = map(int, input().split())
factors = factorize(GCD(a, b))

ans = len(factors) + 1

print(ans)
