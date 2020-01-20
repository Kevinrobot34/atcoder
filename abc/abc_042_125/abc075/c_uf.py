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
edges = []
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append( (a, b) )

ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if i == j:
            continue
        uf.unite(edges[j][0], edges[j][1])

    is_bridge = False
    for j in range(1, n):
        if not uf.same(j-1, j):
            is_bridge = True
            break

    if is_bridge:
        ans += 1

print(ans)
