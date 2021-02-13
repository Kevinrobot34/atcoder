from operator import itemgetter
import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n
        self.n_edges = [0] * n

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
            self.n_edges[x] += self.n_edges[y] + 1
        else:
            self.n_edges[x] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]

    def edges(self, x):
        return self.n_edges[self.root(x)]


n, h, w = map(int, input().split())
uf = UnionFind(h + w)
edges = [tuple(map(int, input().split())) for _ in range(n)]
edges.sort(key=itemgetter(2), reverse=True)

ans = 0
for ri, ci, ai in edges:
    ri -= 1
    ci -= 1
    ci += h
    if not uf.same(ri, ci):
        if uf.edges(ri) + uf.edges(ci) < uf.size(ri) + uf.size(ci):
            ans += ai
            uf.unite(ri, ci)
    else:
        if uf.edges(ri) < uf.size(ri):
            ans += ai
            uf.unite(ri, ci)

print(ans)
