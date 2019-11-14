import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


class Tree():
    def __init__(self, n, graph, v_root):
        self.n = n  # number of nodes
        self.graph = graph  # adjacent list of graph
        self.v_root = v_root  # root node

        self.logn = (self.n - 1).bit_length()
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.depth = [0] * self.n
        # self.dist = [0] * self.n

        self.init()

    def init(self):
        # self.dfs(self.v_root, -1, 0, 0)
        self.dfs(self.v_root, -1, 0)
        # doubling
        for k in range(self.logn - 1):
            for v in range(self.n):
                if self.parent[k][v] != -1:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    # def dfs(self, v, v_par, depth, dist):
    def dfs(self, v, v_par, depth):
        self.parent[0][v] = v_par
        self.depth[v] = depth
        # self.dist[v] = dist
        # for v_next, d in self.graph[v]:
        for v_next in self.graph[v]:
            if v_next == v_par:
                continue
            # self.dfs(v_next, v, depth + 1, dist + d)
            self.dfs(v_next, v, depth + 1)

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u

        # go to parents of v until same depth as u
        diff = self.depth[v] - self.depth[u]
        for k in range(self.logn):
            if diff & (1 << k):
                v = self.parent[k][v]
        if u == v:
            return u
        # binary search
        for k in reversed(range(self.logn)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # graph[x].append((y, 1))
    # graph[y].append((x, 1))
    graph[x].append(y)
    graph[y].append(x)

tree = Tree(n, graph, 0)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    lca = tree.lca(a, b)
    dist = tree.depth[a] + tree.depth[b] - 2 * tree.depth[lca]
    ans = dist + 1
    print(ans)
