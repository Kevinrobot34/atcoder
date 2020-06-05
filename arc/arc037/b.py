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


n, m = map(int, input().split())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

uf = UnionFind(n)
for u, v in edges:
    uf.unite(u, v)

count_edges = [0] * n
for u, v in edges:
    count_edges[uf.root(u)] += 1

ans = 0
for i in range(n):
    if count_edges[uf.root(i)] == uf.size(i) - 1:
        ans += 1
    count_edges[uf.root(i)] = -1
print(ans)
