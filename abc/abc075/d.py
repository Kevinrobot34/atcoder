import sys
from bisect import bisect_left
input = sys.stdin.readline

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

x = [p[i][0] for i in range(n)]
x.sort()
y = [p[i][1] for i in range(n)]
y.sort()

coord = [[0] * n for i in range(n)]
for i in range(n):
    x_idx = bisect_left(x, p[i][0])
    y_idx = bisect_left(y, p[i][1])
    coord[x_idx][y_idx] += 1

coord_cs = [[0] * (n+1) for i in range(n+1)]
for i in range(n):
    for j in range(n):
        coord_cs[i+1][j+1] = coord[i][j]
for i in range(n):
    for j in range(n+1):
        coord_cs[i+1][j] += coord_cs[i][j]
for i in range(n+1):
    for j in range(n):
        coord_cs[i][j+1] += coord_cs[i][j]

# print(*coord, sep='\n')
# print(*coord_cs, sep='\n')

ans = (x[-1] - x[0]) * (y[-1] - y[0])
for xi in range(n):
    for xj in range(xi+1, n+1):
        for yi in range(n):
            for yj in range(yi+1, n+1):
                if coord_cs[xj][yj] - coord_cs[xi][yj] - coord_cs[xj][yi] + coord_cs[xi][yi] == k:
                    cand = (x[xj-1] - x[xi]) * (y[yj-1] - y[yi])
                    ans = min(ans, cand)

print(ans)
