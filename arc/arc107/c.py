from collections import Counter


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


MOD = 998244353
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD

uf_row = UnionFind(n)
uf_col = UnionFind(n)
for i in range(n):
    for j in range(i + 1, n):
        if all(a[i][l] + a[j][l] <= k for l in range(n)):
            uf_row.unite(i, j)
        if all(a[l][i] + a[l][j] <= k for l in range(n)):
            uf_col.unite(i, j)

ans = 1
cnt_row = Counter(uf_row.root(i) for i in range(n))
cnt_col = Counter(uf_col.root(i) for i in range(n))
for v in cnt_row.values():
    ans *= fact[v]
    ans %= MOD
for v in cnt_col.values():
    ans *= fact[v]
    ans %= MOD

print(ans)
