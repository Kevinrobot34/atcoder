n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

a.sort(reverse=True)
f.sort()


def check(x):
    red = 0
    for i in range(n):
        if a[i] * f[i] > x:
            red += a[i] - x // f[i]

    return (red <= k)


lb = -1  # false
ub = max([a[i] * f[i] for i in range(n)])  # true
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
