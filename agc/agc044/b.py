from heapq import heappush, heappop


class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])  # contraction
            return self.par[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.par[x] > self.par[y]:  # merge technique
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sheet = [[1] * n for _ in range(n)]
uf = UnionFind(n**2 + 1)


def solve(x, y):
    q = []
    heappush(q, (0, x, y))
    tmp = [[n**2] * n for _ in range(n)]
    while q:
        c, x, y = heappop(q)
        if x < 0 or x >= n or y < 0 or y >= n:
            return c
        if uf.same(x * n + y, n**2):
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

    ans += z
    sheet[x][y] = 0
    if x == 0 or y == 0 or x == n - 1 or y == n - 1:
        uf.unite(p[i], n**2)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and sheet[nx][ny] == 0:
            uf.unite(p[i], nx * n + ny)

print(ans)
