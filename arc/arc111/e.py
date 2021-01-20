import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def floor_sum(n: int, m: int, a: int, b: int) -> int:
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
    a, b, c, d = map(int, input().split())
    k = (d - 2) // (c - b)
    f1 = floor_sum(k + 1, d, c, a)
    f2 = floor_sum(k + 1, d, b, a - 1)
    ans = k - f1 + f2
    print(ans)
