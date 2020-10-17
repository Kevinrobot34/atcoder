from collections import deque
OFFSETS = 201
MAX = 10**6
dx = [+1, 0, -1, +1, -1, 0]
dy = [+1, +1, +1, 0, 0, -1]

n, gx, gy = map(int, input().split())
gx += OFFSETS
gy += OFFSETS
grid = [[MAX] * (OFFSETS * 2 + 1) for _ in range(OFFSETS * 2 + 1)]
for _ in range(n):
    x, y = map(int, input().split())
    x += OFFSETS
    y += OFFSETS
    grid[x][y] = -1

queue = deque([(OFFSETS, OFFSETS)])
grid[OFFSETS][OFFSETS] = 0

ans = -1
while queue:
    x, y = queue.popleft()
    c = grid[x][y]
    if (x, y) == (gx, gy):
        ans = grid[x][y]
        break
    for k in range(len(dx)):
        nx = x + dx[k]
        ny = y + dy[k]
        if abs(nx - OFFSETS) > OFFSETS or abs(ny - OFFSETS) > OFFSETS:
            continue
        if grid[nx][ny] == -1:
            continue
        if c + 1 < grid[nx][ny]:
            grid[nx][ny] = c + 1
            queue.append((nx, ny))

print(ans)
