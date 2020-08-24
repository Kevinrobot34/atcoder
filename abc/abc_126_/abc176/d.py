from heapq import heappush, heappop
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
ch, cw = map(lambda x: int(x) - 1, input().split())
dh, dw = map(lambda x: int(x) - 1, input().split())
s = [input() for _ in range(h)]

INF = 10**10
cost = [[INF] * w for _ in range(h)]

dxy = [(0, +1, 0), (0, 0, +1), (0, -1, 0), (0, 0, -1)]
dxy += [(1, i, j) for i in [-2, 2] for j in range(-2, 3)]
dxy += [(1, i, j) for j in [-2, 2] for i in range(-1, 2)]
dxy += [(1, -1, -1), (1, -1, +1), (1, +1, -1), (1, +1, +1)]

q = [(0, ch, cw)]
cost[ch][cw] = 0
while q:
    c, x, y = heappop(q)
    if cost[x][y] < c:
        continue

    if x == dh and y == dw:
        break

    for c_, dx_, dy_ in dxy:
        nx = x + dx_
        ny = y + dy_
        nc = c + c_
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if s[nx][ny] == '#':
            continue
        if cost[nx][ny] <= nc:
            continue
        cost[nx][ny] = nc
        heappush(q, (nc, nx, ny))

ans = -1 if cost[dh][dw] == INF else cost[dh][dw]
print(ans)
# print(*cost, sep='\n')
