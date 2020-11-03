from operator import itemgetter


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
points = [tuple(map(int, input().split())) for _ in range(n)]

uf = UnionFind(n + 2)  # 0: y=100, 1: y=-100, others: points
dist = []
dist.append((0, 1, 200.0))
for i in range(n):
    dist.append((0, i + 2, 100.0 - points[i][1]))
    dist.append((1, i + 2, points[i][1] + 100.0))

for i in range(n):
    xi, yi = points[i]
    for j in range(i + 1, n):
        xj, yj = points[j]
        dist.append((i + 2, j + 2, ((xi - xj)**2 + (yi - yj)**2)**0.5))

dist.sort(key=itemgetter(2))
for i, j, d in dist:
    uf.unite(i, j)
    if uf.same(0, 1):
        ans = d / 2.0
        break

print(ans)
