import math
from collections import defaultdict

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i, (xi, yi) in enumerate(xy):
    d = defaultdict(int)
    for j, (xj, yj) in enumerate(xy):
        if i == j:
            continue
        vx = xi - xj
        vy = yi - yj
        if vx < 0 or (vx == 0 and vy < 0):
            vx *= -1
            vy *= -1
        g = math.gcd(vx, vy)
        vx //= g
        vy //= g
        d[(vx, vy)] += 1
    for v in d.values():
        if v > 1:
            cnt += v * (v - 1) // 2

ans = n * (n - 1) * (n - 2) // 6 - cnt // 3
print(ans)
