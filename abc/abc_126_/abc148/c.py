def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)


a, b = map(int, input().split())
ans = LCM(a, b)
print(ans)
