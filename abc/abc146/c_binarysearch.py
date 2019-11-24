a, b, x = map(int, input().split())


def check(n):
    if n == 0:
        return True
    elif n > 10**9:
        return False

    return (a * n + b * len(str(n)) <= x)


lb = 0  # True
ub = 10**9 + 1  # False
while ub - lb > 1:
    mid = (lb + ub) // 2
    if check(mid):
        lb = mid
    else:
        ub = mid

print(lb)
