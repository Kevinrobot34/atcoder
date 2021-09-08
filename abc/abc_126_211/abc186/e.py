from typing import Tuple
from math import gcd


# return (g, x, y) which satisfies ax + by = g and g = GCD(a,b)
def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if b:
        g, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y
    return a, 1, 0


def func(n, s, k):
    g = gcd(n, gcd(s, k))
    n //= g
    s //= g
    k //= g

    # s + xk ≡ 0 (mod n)なるxを求める
    if gcd(k, n) != 1:
        return -1
    else:
        _, ki, _ = ext_gcd(k, n)
        x = (-s) * ki % n
        return x


t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    print(func(n, s, k))
