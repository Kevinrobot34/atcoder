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
        self.dist = [0] * self.n

        self.init()

    def init(self):
        self.dfs(self.v_root, -1, 0, 0)
        # doubling
        for k in range(self.logn - 1):
            for v in range(self.n):
                if self.parent[k][v] != -1:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    def dfs(self, v, v_par, depth, dist):
        self.parent[0][v] = v_par
        self.depth[v] = depth
        self.dist[v] = dist
        for v_next, c, d in self.graph[v]:
            if v_next == v_par:
                continue
            self.dfs(v_next, v, depth + 1, dist + d)

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


n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))

v_root = n // 2
tree = Tree(n, graph, v_root)

query = []
memo = [set() for i in range(n)]
for _ in range(q):
    x, y, u, v = map(int, input().split())
    u -= 1
    v -= 1
    lca_uv = tree.lca(u, v)
    memo[u].add(x)
    memo[v].add(x)
    memo[lca_uv].add(x)

    query.append((x, y, u, v, lca_uv))

n_color = [0] * n
d_color = [0] * n
n_color_memo = {}
d_color_memo = {}


def dfs(v, v_par, dist):
    for c in memo[v]:
        n_color_memo[(v, c)] = n_color[c]
        d_color_memo[(v, c)] = d_color[c]

    for v_next, c, d in graph[v]:
        if v_next == v_par:
            continue
        n_color[c] += 1
        d_color[c] += d
        dfs(v_next, v, dist + d)
        n_color[c] -= 1
        d_color[c] -= d


dfs(v_root, -1, 0)

for x, y, u, v, lca in query:
    depth_u = tree.dist[u]
    depth_u += -d_color_memo[(u, x)] + y * n_color_memo[(u, x)]
    depth_v = tree.dist[v]
    depth_v += -d_color_memo[(v, x)] + y * n_color_memo[(v, x)]
    depth_lca = tree.dist[lca]
    depth_lca += -d_color_memo[(lca, x)] + y * n_color_memo[(lca, x)]

    ans = depth_u + depth_v - 2 * depth_lca
    print(ans)
