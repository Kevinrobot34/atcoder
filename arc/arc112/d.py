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


h, w = map(int, input().split())
s = [input() for _ in range(h)]


def func(s, h, w):
    uf = UnionFind(w)
    uf.unite(0, w - 1)

    # connect horizontal direction
    for i in range(h):
        target = [j for j in range(w) if s[i][j] == '#']
        if i == 0 or i == h - 1:
            target.append(w - 1)
        for j in range(len(target) - 1):
            uf.unite(target[j], target[j + 1])

    return len(set(uf.root(i) for i in range(w) if not uf.same(0, i)))


cand1 = func(s, h, w)
t = [[s[i][j] for i in range(h)] for j in range(w)]
cand2 = func(t, w, h)
ans = min(cand1, cand2)
print(ans)
