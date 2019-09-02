from heapq import heappush, heappop
import sys
from operator import itemgetter
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
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

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append([x, y, i])

edge = []
points.sort(key=itemgetter(0))
for i in range(1, n):
    dist = points[i][0] - points[i-1][0]
    edge.append((points[i][2], points[i-1][2], dist))
    edge.append((points[i-1][2], points[i][2], dist))

points.sort(key=itemgetter(1))
for i in range(1, n):
    dist = points[i][1] - points[i-1][1]
    edge.append((points[i][2], points[i-1][2], dist))
    edge.append((points[i-1][2], points[i][2], dist))

# print(edge)
def kruskal(edge: list) -> int:
    # edge[node] = (v_from, v_to, cost)
    edge.sort(key=itemgetter(2)) # Sort edges by its cost
    uf = UnionFind(n)
    ans = 0
    for v_from, v_to, cost in edge:
        if not uf.same(v_from, v_to):
            ans += cost
            uf.unite(v_from, v_to)
    return ans

print(kruskal(edge))
