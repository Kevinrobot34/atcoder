from collections import deque
h, w = map(int, input().split())
m = [['#']*(w+2)] + [['#']+list(input())+['#'] for _ in range(h)] + [['#']*(w+2)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque([(1, 1, 1)])
m[1][1] = '@'
ans = -1
while q:
    x, y, c = q.popleft()
    if x == h and y == w:
        ans = c
        break
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if m[nx][ny] == '.':
            q.append((nx, ny, c+1))
            m[nx][ny] = '@'

if ans != -1:
    for i in range(1, h+1):
        for j in range(1, w+1):
            if m[i][j] == '#':
                ans += 1
    ans = h*w - ans

print(ans)
