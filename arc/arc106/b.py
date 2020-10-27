import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


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
a = list(map(int, input().split()))
b = list(map(int, input().split()))
uf = UnionFind(n)
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    uf.unite(c, d)

connected = defaultdict(list)
for i in range(n):
    connected[uf.root(i)].append(i)

is_possible = True
for val in connected.values():
    x = sum(a[vi] for vi in val)
    y = sum(b[vi] for vi in val)
    if x != y:
        is_possible = False
        break

ans = 'Yes' if is_possible else 'No'
print(ans)
