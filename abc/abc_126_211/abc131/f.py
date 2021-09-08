from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x]) # contruction
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[x] = y

    def same(self, x, y):
        return self.find(x) ==  self.find(y)


n = int(input())

uf = UnionFind(n)
xs = []
ys = []
x_dict = {}
y_dict = {}
for i in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

    if x in x_dict:
        uf.unite(i, x_dict[x])

    if y in y_dict:
        uf.unite(i, y_dict[y])

    x_dict[x] = uf.find(i)
    y_dict[y] = uf.find(i)

# print(uf.par)
xi = defaultdict(list)
yi = defaultdict(list)
for i in range(n):
    xi[uf.find(x_dict[xs[i]])].append(xs[i])
    yi[uf.find(y_dict[ys[i]])].append(ys[i])

ans = 0
for k in xi.keys():
    ans += len(set(xi[k])) * len(set(yi[k])) - len(xi[k])

print(ans)
