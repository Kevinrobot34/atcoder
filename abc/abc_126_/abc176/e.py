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


h, w, m = map(int, input().split())
bombs = [tuple(map(int, input().split())) for _ in range(m)]

x_dict = {}
y_dict = {}
uf = UnionFind(m)
for i in range(m):
    x, y = map(int, input().split())
    if x in x_set:
        uf.unite(i, x_dict[x])
    else:
        x_dict[x] = i

    if y in y_set:
        uf.unite(i, y_dict[y])
    else:
        y_dict[y] = i
