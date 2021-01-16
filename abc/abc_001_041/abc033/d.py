import sys
import math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
EPS = 1e-10

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

ans2 = ans3 = 0
for i, (xi, yi) in enumerate(p):
    arg = []
    for j, (xj, yj) in enumerate(p):
        if i == j:
            continue
        th = math.atan2(yj - yi, xj - xi)
        arg.append(th)
        arg.append(th + math.pi * 2)
    arg.sort()
    for j, (xj, yj) in enumerate(p):
        if i == j:
            continue
        th = math.atan2(yj - yi, xj - xi)

        # 鈍角
        ans3 += bisect_left(arg, th + math.pi - EPS) - bisect_left(
            arg, th + math.pi / 2 + EPS)

        # 直角
        ans2 += bisect_left(arg, th + math.pi / 2 + EPS) - bisect_left(
            arg, th + math.pi / 2 - EPS)

ans1 = n * (n - 1) * (n - 2) // 6 - ans2 - ans3
print(ans1, ans2, ans3)
