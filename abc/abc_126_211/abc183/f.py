from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


class UnionFind():
    def __init__(self, n, c_init):
        self.par = [-1] * n
        self.cnt = [defaultdict(int) for _ in range(n)]
        for i, ci in enumerate(c_init):
            self.cnt[i][ci] += 1

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
            for k, v in self.cnt[y].items():
                self.cnt[x][k] += v
            self.cnt[y] = defaultdict(int)
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


n, q = map(int, input().split())
c = list(map(lambda x: int(x) - 1, input().split()))
uf = UnionFind(n, c)
# print(*uf.cnt, sep='\n')
for _ in range(q):
    query = input()
    if query[0] == '1':
        _, a, b = map(int, query.split())
        a -= 1
        b -= 1
        uf.unite(a, b)
    else:
        _, x, y = map(int, query.split())
        x -= 1
        y -= 1
        print(uf.cnt[uf.root(x)][y])

# print(uf.par)
# print(*uf.cnt, sep='\n')
