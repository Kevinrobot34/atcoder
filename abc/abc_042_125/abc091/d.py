from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for k in range(29):
        t = 1 << k
        cnt = 0
        b_ = list(map(lambda x: x % (2 * t), b))
        b_.sort()
        for ai in a:
            ai %= 2 * t
            cnt += bisect_left(b_, 2 * t - ai) - bisect_left(b_, t - ai)
            cnt += bisect_left(b_, 4 * t - ai) - bisect_left(b_, 3 * t - ai)

        # print(k, cnt)
        if cnt % 2 == 1:
            ans |= t

    print(ans)


if __name__ == '__main__':
    main()
