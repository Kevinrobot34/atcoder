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


n = int(input())
MAX = 400_000 + 5
uf = UnionFind(MAX)
for _ in range(n):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    uf.unite(ai, bi)

cc_set = set(uf.root(i) for i in range(MAX))
ans = 0
for v in cc_set:
    m = uf.size(v)
    ans += m if uf.n_edges[v] >= m else m - 1

print(ans)
