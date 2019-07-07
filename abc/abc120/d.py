class UnionFind():
    def __init__(self, n):
        self.par = [-1 for i in range(n)]

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # contraction
            return self.par[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.par[x] > self.par[y]: # merge technique
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


n, m = map(int, input().split())
edge = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

uf = UnionFind(n)
ans = n * (n-1) // 2
anss = []
for i in reversed(range(m)):
    anss.append(ans)
    # print(uf.par)
    # print(uf.size, [uf.size[uf.find(i)] for i in range(n)])
    a, b = edge[i]
    if not uf.same(a, b):
        ans -= uf.size(a) * uf.size(b)
    # print(i, a, b)

    uf.unite(a, b)

for i in reversed(range(m)):
    print(anss[i])
