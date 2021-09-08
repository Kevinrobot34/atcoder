import sys
sys.setrecursionlimit(10**6)

n = 100 + 5
a, b, c = map(int, input().split())

memo = {}


def func(x, y, z):
    if x == 100 or y == 100 or z == 100:
        return 0.0

    if (x, y, z) not in memo:
        memo[(x, y, z)] = (x * (func(x + 1, y, z) + 1) + y *
                           (func(x, y + 1, z) + 1) + z *
                           (func(x, y, z + 1) + 1)) / (x + y + z)

    return memo[(x, y, z)]


print(func(a, b, c))
