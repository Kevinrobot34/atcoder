from heapq import heappush, heappop
h, w, t = map(int, input().split())
s = [['@'] * (w + 2)]
s += [list('@' + input() + '@') for _ in range(h)]
s += [['@'] * (w + 2)]
INF = t + 1
dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]
# print(*s, sep='\n')

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == 'S':
            sx, sy = i, j
        elif s[i][j] == 'G':
            gx, gy = i, j
            s[i][j] = '.'


def check(x):
    time = [[INF] * (w + 2) for i in range(h + 2)]
    time[sx][sy] = 0
    queue = [(0, sx, sy)]
    while queue:
        ct, cx, cy = heappop(queue)
        if cx == gx and cy == gy:
            break
        if ct > t:
            break
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if s[nx][ny] == '@':
                continue

            if s[nx][ny] == '.' and ct + 1 < time[nx][ny]:
                time[nx][ny] = ct + 1
                queue.append((ct + 1, nx, ny))
            elif s[nx][ny] == '#' and ct + x < time[nx][ny]:
                time[nx][ny] = ct + x
                queue.append((ct + x, nx, ny))

    return time[gx][gy] <= t


lb = 1  # True
ub = t + 1  # False
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        lb = mid
    else:
        ub = mid

print(lb)
