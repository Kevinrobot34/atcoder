import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def floor_sum(n: int, m: int, a: int, b: int) -> int:
    # references
    # - https://github.com/atcoder/ac-library/blob/c36e178c126110d319b7781d1e875bc6faed36a2/atcoder/math.hpp#L82-L97
    # - https://rsk0315.hatenablog.com/entry/2020/12/13/231307
    ans = 0
    if a >= m:
        ans += n * (n - 1) // 2 * (a // m)
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    last = a * n + b
    if last >= m:
        ans += floor_sum(last // m, a, m, last % m)

    return ans


t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
