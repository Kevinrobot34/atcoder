import sys
input = sys.stdin.readline


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
uf = UnionFind(nx * ny)
for x in range(nx):
    for y in range(ny):
        c0 = x * ny + y
        # print(x, y, c0)
        if y + 1 < ny and v_ng[x][y + 1] == 0:
            c1 = x * ny + (y + 1)
            uf.unite(c0, c1)
        if x + 1 < nx and h_ng[x + 1][y] == 0:
            c2 = (x + 1) * ny + y
            uf.unite(c0, c2)

c_start = x_zipped[0] * ny + y_zipped[0]
if uf.same(c_start, 0):
    ans = 'INF'
else:
    ans = 0
    for x in range(nx):
        for y in range(ny):
            if uf.same(c_start, x * ny + y):
                ans += (x_unzipped[x + 1] -
                        x_unzipped[x]) * (y_unzipped[y + 1] - y_unzipped[y])

print(ans)
