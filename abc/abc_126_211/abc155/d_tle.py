from bisect import bisect_left, bisect_right
import sys


def main():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = tuple(a)

    def check(x):
        # k番目の数がx以下であるか
        # x以下の数字がk個以上あるか
        cnt = 0
        for i, ai in enumerate(a):
            if ai > 0:
                idx = bisect_right(a, x // ai)
                cnt += max(idx - i - 1, 0)
            elif ai < 0:
                idx = bisect_left(a, -(x // abs(ai)))
                # cnt += n - idx
                cnt += n - max(idx, i + 1)
            else:
                # ai == 0
                if x >= 0:
                    cnt += n - i - 1

            if cnt >= k:
                return True
        # print('check', x, cnt)
        return cnt >= k

    # lb = -10**18  # False
    # ub = +10**18  # True
    lb = min(a[0]**2, a[0] * a[-1], a[-1]**2) - 1  # False
    ub = max(a[0]**2, a[0] * a[-1], a[-1]**2) + 1  # True

    while ub - lb > 1:
        mid = (ub + lb) // 2
        # print(lb, ub)
        if check(mid):
            ub = mid
        else:
            lb = mid

    print(ub)


if __name__ == '__main__':
    main()
