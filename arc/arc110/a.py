from functools import reduce


def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)


n = int(input())
ans = reduce(LCM, range(1, n + 1)) + 1
print(ans)
