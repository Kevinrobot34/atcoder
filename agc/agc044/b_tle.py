from heapq import heappush, heappop

n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sheet = [[1] * n for _ in range(n)]


def solve(x, y):
    q = []
    heappush(q, (0, x, y))
    tmp = [[float('inf')] * n for _ in range(n)]
    while q:
        c, x, y = heappop(q)
        if x < 0 or x >= n or y < 0 or y >= n:
            return c
        if tmp[x][y] <= c:
            continue
        tmp[x][y] = c
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                heappush(q, (c, nx, ny))
            else:
                heappush(q, (c + sheet[nx][ny], nx, ny))


ans = 0
for i in range(n**2):
    x, y = p[i] // n, p[i] % n
    z = solve(x, y)
    # if z > 0:
    #     print(z, i, p[i], x, y)
    ans += z
    sheet[x][y] = 0

print(ans)
