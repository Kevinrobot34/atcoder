from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
# print(a)

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[n - 1 - i]


def check(x):
    # M回の握手の幸福度の最小値をx以上にできるか
    # つまり、M回の任意の握手の幸福度をx以上にできるか
    cnt = 0
    for ai in a:
        idx = bisect_left(a, x - ai)
        cnt += n - idx
    return cnt >= m


lb = 1  # True
ub = 2 * a[-1] + 5  # False
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        lb = mid
    else:
        ub = mid

# print(lb)

ans = 0
cnt = 0
for ai in a:
    idx = bisect_left(a, lb - ai)
    ans += ai * (n - idx) + a_cs[n - idx]
    cnt += n - idx
ans -= lb * (cnt - m)
print(ans)
