n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
eps = 1e-6
l = sum(ai for ai, _ in ab)


def check(x: float) -> bool:
    # check if left side time < right side time
    lt = rt = 0.0
    y = 0.0
    for ai, bi in ab:
        if y + ai <= x:
            lt += ai / bi
        elif y <= x < y + ai:
            lt += (x - y) / bi
            rt += (y + ai - x) / bi
        else:
            rt += ai / bi

        y += ai
    return lt < rt


lb = 0.0  # True
ub = l  # False
while ub - lb > eps:
    mid = (ub + lb) / 2.0
    if check(mid):
        lb = mid
    else:
        ub = mid

print(lb)
