n, m = map(int, input().split())
a = list(map(int, input().split()))


def check(x):
    # mex minがx以下であるかどうか
    cnt = [0] * n
    kinds = 0  # x以下の数がいくつ使われているか
    for i, ai in enumerate(a):
        if i >= m:
            if a[i - m] <= x and cnt[a[i - m]] == 1:
                kinds -= 1
            cnt[a[i - m]] -= 1
        if ai <= x and cnt[ai] == 0:
            kinds += 1
        cnt[ai] += 1

        if i >= m - 1 and kinds <= x:
            return True
    return False


lb = -1  # False
ub = n  # True
while ub - lb > 1:
    mid = (lb + ub) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid
print(ub)
