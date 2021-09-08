from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


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


MAX = 10**5 + 1
n = int(input())
uf = UnionFind(MAX * 2)
x_set = set()
y_set = set()
for _ in range(n):
    xi, yi = map(int, input().split())
    yi += MAX
    uf.unite(xi, yi)
    x_set.add(xi)
    y_set.add(yi)

root_nx = defaultdict(int)
root_ny = defaultdict(int)
for xi in x_set:
    root_nx[uf.root(xi)] += 1
for yi in y_set:
    root_ny[uf.root(yi)] += 1

ans = sum(root_nx[i] * root_ny[i] for i in root_nx) - n
print(ans)
