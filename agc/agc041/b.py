n, m, v, p = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


def check(x):
    if x > n - p:
        return True

    for i in range(x + 1, n - p + 1):
        if a[x] + m < a[i]:
            return False

    if v - x - p > 0:
        cnt = 0
        for i in range(x + 1, n - p + 1):
            cnt += min((a[x] + m) - a[i], m)

        if (cnt // (v - x - p)) >= m:
            return True
        else:
            return False
    else:
        return True


lb = -1  # False
ub = n - 1  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

# print(a)
# print(lb, ub)
ans = n - ub
print(ans)
