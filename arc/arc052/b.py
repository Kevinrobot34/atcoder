import math
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
cones = [tuple(map(int, input().split())) for _ in range(n)]


def func(x, r, h, x2):
    if x2 <= x:
        return 0.0
    else:
        total = (math.pi * r**2) * h / 3.0
        h2 = max(x + h - x2, 0)
        return total * (1 - (h2 / h)**3)


X_MAX = (2 * 10**4) + 1
v_cs = [0] * (X_MAX + 1)  # v_cs[i] = (x座標が[0, i)の範囲の体積)
for i in range(1, X_MAX + 1):
    for x, r, h in cones:
        v_cs[i] += func(x, r, h, i - 1)

for _ in range(q):
    a, b = map(int, input().split())
    ans = v_cs[b + 1] - v_cs[a + 1]
    print(ans)
