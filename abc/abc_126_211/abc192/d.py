x = list(map(int, list(input())))
m = int(input())

n = len(x)
d = max(list(x))


def check(a):
    # xをa進数として見た際にm以下であるか
    y = 0
    for xi in x:
        y *= a
        y += xi
        if y > m:
            return False
    return True


if n == 1:
    ans = 1 if x[0] <= m else 0
elif check(d + 1) and d < m:
    lb = d + 1  # True
    ub = m + 1  # False
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check(mid):
            lb = mid
        else:
            ub = mid
    ans = ub - (d + 1)
else:
    ans = 0

print(ans)
