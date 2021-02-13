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


h, w = map(int, input().split())
s = [input() for _ in range(h)]

uf = UnionFind(h + w)
uf.unite(0, h)  # (0, 0)
uf.unite(h - 1, h)  # (h-1, 0)
uf.unite(0, h + w - 1)  # (0, w-1)
uf.unite(h - 1, h + w - 1)  # (h-1, w-1)
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            uf.unite(i, h + j)

ans = min(
    len(set(uf.root(i) for i in range(h))) - 1,
    len(set(uf.root(i) for i in range(h, h + w))) - 1,
)
print(ans)
