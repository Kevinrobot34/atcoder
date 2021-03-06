class UnionFind():
    def __init__(self, n):
        self.par = [-1 for i in range(n)]

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


n, m, k = map(int, input().split())
n_friends = [0] * n
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    uf.unite(a, b)
    n_friends[a] += 1
    n_friends[b] += 1

ans = [uf.size(i) - 1 - n_friends[i] for i in range(n)]

for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.same(c, d):
        ans[c] -= 1
        ans[d] -= 1

print(*ans)
