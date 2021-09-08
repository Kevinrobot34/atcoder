from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

a_minus = a_zero = a_plus = 0
for i in range(n):
    if a[i] > 0:
        a_plus += 1
    elif a[i] == 0:
        a_zero += 1
    else:
        a_minus += 1

aa_minus = a_minus * a_plus
aa_zero = a_zero * (n - a_zero) + a_zero * (a_zero - 1) // 2


def check_minus(x):
    # k番目の数がx(<0)以下であるか
    # x以下の数字がk個以上あるか
    cnt = 0
    j = a_minus + a_zero
    for i in range(a_minus):
        # a[i] < 0
        while j < n and a[i] * a[j] > x:
            j += 1
        cnt += n - j

    return cnt >= k


def check_plus(x):
    # k番目の数がx(>0)以下であるか
    # x以下の数字がk個以上あるか

    def func(b, m):
        # 昇順ソート済みの数列b (長さm)
        # 掛け算してx以下となる数を求める
        c = 0
        j = m - 1
        for i in range(m):
            while j > 0 and b[i] * b[j] > x:
                j -= 1
            c += max(j - i, 0)
        return c

    cnt = aa_minus + aa_zero
    cnt += func(a[-a_plus:], a_plus)
    cnt += func(list(reversed(a[:a_minus])), a_minus)
    return cnt >= k


if k <= aa_minus:
    # k番目の数は負の数
    lb = a[0] * a[-1] - 1  # False
    ub = 0  # True
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check_minus(mid):
            ub = mid
        else:
            lb = mid

    ans = ub
elif k <= aa_minus + aa_zero:
    # k番目の数は0
    ans = 0
else:
    # k番目の数はプラス
    lb = 0  # False
    ub = max(a[0]**2, a[-1]**2) + 1  # True
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check_plus(mid):
            ub = mid
        else:
            lb = mid

    ans = ub

print(ans)
