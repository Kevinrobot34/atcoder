from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[x] = y

    def same(self, x, y):
        return self.find(x) ==  self.find(y)


n, m = map(int, input().split())
p = list(map(int, input().split()))
p = [v-1 for v in p]

uf = UnionFind(n)
for _ in range(m):
    x, y = map(int, input().split())
    uf.unite(x-1, y-1)

ans = 0
for i in range(n):
    if uf.same(i, p[i]):
        ans += 1

print(ans)
