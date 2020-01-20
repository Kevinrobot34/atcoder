from operator import itemgetter
import sys
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
query = []
year = []
for i in range(m):
    a, b, y = map(int, input().split())
    query.append([
        -y,
        0,
        a,
        b,
    ])

q = int(input())
for i in range(q):
    v, w = map(int, input().split())
    w += 1
    query.append([
        -w,
        1,
        v,
        i,
    ])

query.sort()
uf = UnionFind(n + 1)
ans = [0] * q
for qi in query:
    # print(len(qi), qi)
    if qi[1] == 0:
        y, _, a, b = qi
        uf.unite(a, b)
    else:
        w, _, v, i = qi
        ans[i] = uf.size(v)

print(*ans, sep='\n')
