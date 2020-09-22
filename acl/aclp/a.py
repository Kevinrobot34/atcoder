import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


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


n, q = map(int, input().split())
uf = UnionFind(n)
for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        # add
        uf.unite(u, v)
    else:
        print(1 if uf.same(u, v) else 0)
