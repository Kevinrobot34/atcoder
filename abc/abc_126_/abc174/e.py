n, k = map(int, input().split())
a = list(map(int, input().split()))


def check(x):
    # 最長の丸太をx以下にできるか
    # 任意の丸太をx以下にできるか
    cnt = sum([(ai - 1) // x for ai in a])
    return cnt <= k


lb = 0  # False
ub = max(a)  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
