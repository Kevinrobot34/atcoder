import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

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

n, k, l = map(int, input().split())
uf_r = UnionFind(n)
for i in range(k):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    uf_r.unite(p, q)
uf_t = UnionFind(n)
for i in range(l):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    uf_t.unite(r, s)

root_r = defaultdict(set)
root_t = defaultdict(set)
for i in range(n):
    root_r[uf_r.root(i)].add(i)
    root_t[uf_t.root(i)].add(i)

ans = []
memo = defaultdict(int)
for i in range(n):
    memo[(uf_r.root(i), uf_t.root(i))] += 1
for i in range(n):
    ans.append(memo[(uf_r.root(i), uf_t.root(i))])

print(*ans)
