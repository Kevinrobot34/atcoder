import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


class Tree():
    def __init__(self, n, v_root):
        self.n = n  # number of nodes
        self.v_root = v_root  # root node

        self.graph = [[] for _ in range(self.n)]  # adjacent list of graph

        self.logn = (self.n - 1).bit_length()
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.depth = [0] * self.n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def init(self):
        self.dfs(self.v_root, -1, 0)
        # doubling
        for k in range(self.logn - 1):
            for v in range(self.n):
                if self.parent[k][v] != -1:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    def dfs(self, v, v_par, depth):
        self.parent[0][v] = v_par
        self.depth[v] = depth
        for v_next in self.graph[v]:
            if v_next == v_par:
                continue
            self.dfs(v_next, v, depth + 1)

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u

        # go to parents of v until same depth as u
        diff = self.depth[v] - self.depth[u]
        for k in range(diff.bit_length()):
            if diff & (1 << k):
                v = self.parent[k][v]
        if u == v:
            return u
        # binary search
        # for k in reversed(range(self.logn)):
        for k in range(self.depth[u].bit_length() - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


n = int(input())
tree = Tree(n, 0)
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    tree.add_edge(x, y)

tree.init()

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    lca = tree.lca(a, b)
    dist = tree.depth[a] + tree.depth[b] - 2 * tree.depth[lca]
    ans = dist + 1
    print(ans)
