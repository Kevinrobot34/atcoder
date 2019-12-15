from bisect import bisect_right
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()


def check(x):
    # x以下の要素数を数える
    cnt = sum(bisect_right(b, x // ai) for ai in a)
    return cnt >= k


lb = 0  # False
ub = a[-1] * b[-1] + 1  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
