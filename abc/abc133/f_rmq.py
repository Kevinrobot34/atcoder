import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


class SegmentTree1():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, operation_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n)  # binary tree
        self.ele_id = ele_id  # identity element
        self.operation_func = operation_func  # binary operation of monoid

    def __getitem__(self, idx):
        return self.data[idx + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.operation_func(self.data[2 * i],
                                               self.data[2 * i + 1])

    def update(self, idx, x):
        # change idx-th element to x (idx : 0-indexed)
        idx += self.n
        self.data[idx] = x
        while idx > 1:
            idx = idx >> 1
            self.data[idx] = self.operation_func(self.data[2 * idx],
                                                 self.data[2 * idx + 1])

    def query(self, l, r):
        # query for interval [l, r) (l, r : 0-indexed)
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l & 1:  # right child
                ret = self.operation_func(ret, self.data[l])
                l += 1
            if r & 1:  # right child
                r -= 1
                ret = self.operation_func(ret, self.data[r])
            # go to parent-nodes
            l = l >> 1
            r = r >> 1
        return ret


class Tree():
    def __init__(self, n, graph, v_root):
        self.n = n  # number of nodes
        self.graph = graph  # adjacent list of graph
        self.v_root = v_root  # root node

        # euler tour
        self.first_idx = [2 * self.n] * self.n
        self.euler_tour = []
        self.euler_depth_topo = []
        self.euler_depth_real = []
        self.euler_tour_dfs(self.v_root, -1, 0, 0)

        depth_list = [(di, i) for i, di in enumerate(self.euler_depth_topo)]
        INF = (2 * self.n, -1)
        operation_func = lambda a, b: a if a[0] < b[0] else b
        self.st_rmq = SegmentTree1(2 * self.n - 1, INF, operation_func)
        self.st_rmq.build(depth_list)

    def euler_tour_dfs(self, v, v_par, depth_topo, depth_real):
        self.first_idx[v] = len(self.euler_tour)
        self.euler_tour.append(v)
        self.euler_depth_topo.append(depth_topo)
        self.euler_depth_real.append(depth_real)
        for v_next, c, d in self.graph[v]:
            if v_next == v_par:
                continue
            self.euler_tour_dfs(v_next, v, depth_topo + 1, depth_real + d)
            self.euler_tour.append(v)
            self.euler_depth_topo.append(depth_topo)
            self.euler_depth_real.append(depth_real)

    def depth_topo(self, v):
        return self.euler_depth_topo[self.first_idx[v]]

    def depth_real(self, v):
        return self.euler_depth_real[self.first_idx[v]]

    def lca(self, u, v):
        u_idx, v_idx = self.first_idx[u], self.first_idx[v]
        if u_idx > v_idx:
            u_idx, v_idx = v_idx, u_idx
        _, idx = self.st_rmq.query(u_idx, v_idx + 1)
        return self.euler_tour[idx]


n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))

tree = Tree(n, graph, 0)

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


def dfs(v, v_par, depth):
    for c in memo[v]:
        n_color_memo[(v, c)] = n_color[c]
        d_color_memo[(v, c)] = d_color[c]

    for v_next, c, d in graph[v]:
        if v_next == v_par:
            continue
        n_color[c] += 1
        d_color[c] += d
        dfs(v_next, v, depth + d)
        n_color[c] -= 1
        d_color[c] -= d


dfs(0, -1, 0)

for x, y, u, v, lca in query:
    depth_u = tree.depth_real(u)
    depth_u += -d_color_memo[(u, x)] + y * n_color_memo[(u, x)]
    depth_v = tree.depth_real(v)
    depth_v += -d_color_memo[(v, x)] + y * n_color_memo[(v, x)]
    depth_lca = tree.depth_real(lca)
    depth_lca += -d_color_memo[(lca, x)] + y * n_color_memo[(lca, x)]

    ans = depth_u + depth_v - 2 * depth_lca
    print(ans)
