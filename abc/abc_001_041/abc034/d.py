n, k = map(int, input().split())
sw = [tuple(map(int, input().split())) for _ in range(n)]


def check(x):
    y = [(pi - x) * wi for (wi, pi) in sw]
    y.sort(reverse=True)
    return sum(y[:k]) >= 0


lb = 0.0
ub = 100.0
while ub - lb > 1e-8:
    mid = (ub + lb) / 2.0
    if check(mid):
        lb = mid
    else:
        ub = mid

print(lb)
