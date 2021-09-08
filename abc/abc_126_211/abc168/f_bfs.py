import sys
from collections import deque
input = sys.stdin.readline


def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=key, reverse=reverse)):
        zipped[xi] = i
        unzipped[i] = xi
    return zipped, unzipped


n, m = map(int, input().split())
line_v = [tuple(map(int, input().split())) for _ in range(n)]
line_h = [tuple(map(int, input().split())) for _ in range(m)]

INF = 10**9 + 10
dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]

x_list = [-INF, 0, INF]
y_list = [-INF, 0, INF]
for x1, x2, y in line_v:
    # abc
    x_list.append(x1)
    x_list.append(x2)
    y_list.append(y)
for x, y1, y2 in line_h:
    # def
    x_list.append(x)
    y_list.append(y1)
    y_list.append(y2)

x_zipped, x_unzipped = compress_coordinate(x_list)
y_zipped, y_unzipped = compress_coordinate(y_list)

nx = len(x_zipped)
ny = len(y_zipped)

v_ng = [[0] * (ny + 1) for _ in range(nx + 1)]
h_ng = [[0] * (ny + 1) for _ in range(nx + 1)]
for x1, x2, y in line_v:
    x1 = x_zipped[x1]
    x2 = x_zipped[x2]
    y = y_zipped[y]
    v_ng[x1][y] += 1
    v_ng[x2][y] -= 1
for x, y1, y2 in line_h:
    x = x_zipped[x]
    y1 = y_zipped[y1]
    y2 = y_zipped[y2]
    h_ng[x][y1] += 1
    h_ng[x][y2] -= 1

for x in range(nx):
    for y in range(ny):
        v_ng[x + 1][y] += v_ng[x][y]
        h_ng[x][y + 1] += h_ng[x][y]

# print(nx, ny)
grid = [[False] * (ny + 1) for _ in range(nx + 1)]
q = deque([(x_zipped[0], y_zipped[0])])
while q:
    x0, y0 = q.popleft()
    if grid[x0][y0]:
        continue
    grid[x0][y0] = True
    for k in range(4):
        x1 = x0 + dx[k]
        y1 = y0 + dy[k]
        if x1 < 0 or x1 >= nx or y1 < 0 or y1 >= ny:
            continue
        if grid[x1][y1]:
            continue

        if k == 0 and h_ng[x1][y1] == 0:
            # move x-dir
            q.append((x1, y1))
        elif k == 2 and h_ng[x0][y0] == 0:
            # move x-dir
            q.append((x1, y1))
        elif k == 1 and v_ng[x1][y1] == 0:
            # move y-dir
            q.append((x1, y1))
        elif k == 3 and v_ng[x0][y0] == 0:
            # move y-dir
            q.append((x1, y1))

# print(*grid, sep='\n')
if grid[0][0]:
    ans = 'INF'
else:
    ans = 0
    for x in range(nx):
        for y in range(ny):
            if grid[x][y]:
                ans += (x_unzipped[x + 1] -
                        x_unzipped[x]) * (y_unzipped[y + 1] - y_unzipped[y])

print(ans)
