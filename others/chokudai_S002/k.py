from itertools import chain
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


def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=None, reverse=reverse)):
        zipped[xi] = i
        unzipped[i] = xi
    return zipped, unzipped


n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

zipped, unzipped = compress_coordinate(chain.from_iterable(ab))
m = len(zipped)
uf = UnionFind(m)
for ai, bi in ab:
    uf.unite(zipped[ai], zipped[bi])

cc_set = set(uf.root(i) for i in range(m))
ans = 0
for v in cc_set:
    n_v = uf.size(v)
    n_e = uf.n_edges[v]
    ans += n_v if n_e >= n_v else n_v - 1

print(ans)
