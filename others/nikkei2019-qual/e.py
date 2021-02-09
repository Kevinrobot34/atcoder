from operator import itemgetter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


class UnionFind():
    def __init__(self, n, w):
        self.par = [-1] * n
        self.weight = w

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
            self.weight[x] += self.weight[y]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


n, m = map(int, input().split())
x = list(map(int, input().split()))
abyi = []
graph = [[] for _ in range(n)]
for i in range(m):
    ai, bi, yi = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append((yi, bi, i))
    graph[bi].append((yi, ai, i))
    abyi.append((ai, bi, yi, i))

abyi.sort(key=itemgetter(2))
uf = UnionFind(n, x)

cand = set()
for ai, bi, yi, i in abyi:
    uf.unite(ai, bi)

    if uf.weight[uf.root(ai)] >= yi:
        cand.add(i)

abyi = abyi[::-1]
ok = [False] * m


def dfs(v, x):
    for cost, v_to, i in graph[v]:
        if cost > x or ok[i]:
            continue
        ok[i] = True
        dfs(v_to, x)


for ai, bi, yi, i in abyi:
    if not ok[i] and i in cand:
        dfs(ai, yi)

ans = m - sum(ok)
print(ans)
