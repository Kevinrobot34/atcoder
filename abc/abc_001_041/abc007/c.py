from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for _ in range(r)]
sy, sx = sy - 1, sx - 1
gy, gx = gy - 1, gx - 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([(sy, sx, 0)])
maze[sy][sx] = '#'
while queue:
    cy, cx, cc = queue.popleft()
    if cy == gy and cx == gx:
        ans = cc
        break

    for k in range(4):
        ny = cy + dy[k]
        nx = cx + dx[k]
        if maze[ny][nx] == '#':
            continue
        else:
            queue.append((ny, nx, cc + 1))
            maze[ny][nx] = '#'

print(ans)
