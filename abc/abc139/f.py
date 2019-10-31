from math import atan2, pi, sqrt
n = int(input())
p = []
xa = ya = 0
for i in range(n):
    x, y = map(int, input().split())
    angle = atan2(y, x)
    p.append((x, y, angle))
    p.append((x, y, angle + 2 * pi))
    xa += x
    ya += y

p.sort(key=lambda x: x[2])

r = 0
ans = 0
xs = ys = 0
for l in range(n):
    while p[r][2] < p[l][2] + pi:
        xs += p[r][0]
        ys += p[r][1]
        r += 1

    ans = max(ans, sqrt(xs**2 + ys**2), sqrt((xa - xs)**2 + (ya - ys)**2))

    xs -= p[l][0]
    ys -= p[l][1]

print(ans)
