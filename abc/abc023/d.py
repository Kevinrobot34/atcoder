n = int(input())
balloon = [tuple(map(int, input().split())) for _ in range(n)]


def check(x):
    # ペナルティーの最大値をx以下にできるかどうかを判定する
    penalty = [(x - hi) / si for (hi, si) in balloon]
    penalty.sort()
    for i, ti in enumerate(penalty):
        if ti < i:
            return False
    return True


lb = 0  # False
ub = 10**14  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
