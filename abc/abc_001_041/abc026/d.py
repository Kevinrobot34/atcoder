import math
a, b, c = map(int, input().split())


def check(t):
    if a * t + b * math.sin(c * t * math.pi) > 100:
        return True
    else:
        return False


lb = 0.0  # False
ub = (100.0 + b) / a + 1.0  # True
EPS = (10**(-7)) / (a + b * c * math.pi)
while ub - lb > EPS:
    # print(lb, ub)
    mid = (ub + lb) / 2.0
    if check(mid):
        ub = mid
    else:
        lb = mid

print(lb)
