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


n = int(input())
s1 = input()
s2 = input()

d1 = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(26)]
d2 = {d1[i]: i for i in range(len(d1))}
is_in = [False] * len(d1)

uf = UnionFind(len(d1))
for i in range(n):
    is_in[d2[s1[i]]] = True
    is_in[d2[s2[i]]] = True
    if s1[i] != s2[i]:
        uf.unite(d2[s1[i]], d2[s2[i]])

ans = 1
is_used = [False] * len(d1)
r0 = uf.root(d2[s1[0]])
for i in range(len(d1)):
    if not is_in[i]:
        continue
    r = uf.root(i)
    if not is_used[r]:
        is_used[r] = True
        if i < 10:
            ans *= 1
        else:
            if r == r0:
                ans *= 9
            else:
                ans *= 10

print(ans)
