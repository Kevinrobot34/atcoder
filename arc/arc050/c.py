import numpy as np


def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


def func(n: int, d: int, MOD: int) -> int:
    mat = np.array([[pow(10, d, MOD), 1], [0, 1]])
    v = np.array([0, 1]).T
    while n > 0:
        if n % 2 == 1:
            v = np.dot(mat, v) % MOD
        mat = np.dot(mat, mat) % MOD
        n //= 2
    return v[0]


a, b, m = map(int, input().split())

d = GCD(a, b)
ans = func(a, 1, m) * func(b // d, d, m) % m
print(ans)
