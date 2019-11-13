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
        self.euler_depth = []
        self.euler_tour_dfs(self.v_root, -1, 0)

        depth_list = [(di, i) for i, di in enumerate(self.euler_depth)]
        INF = (2 * self.n, -1)
        operation_func = lambda a, b: a if a[0] < b[0] else b
        self.st_rmq = SegmentTree1(2 * self.n - 1, INF, operation_func)
        self.st_rmq.build(depth_list)

    def euler_tour_dfs(self, v, v_par, depth):
        self.first_idx[v] = len(self.euler_tour)
        self.euler_tour.append(v)
        self.euler_depth.append(depth)
        for v_next in self.graph[v]:
            if v_next == v_par:
                continue
            self.euler_tour_dfs(v_next, v, depth + 1)
            self.euler_tour.append(v)
            self.euler_depth.append(depth)

    def depth(self, v):
        return self.euler_depth[self.first_idx[v]]

    def lca(self, u, v):
        u_idx, v_idx = self.first_idx[u], self.first_idx[v]
        if u_idx > v_idx:
            u_idx, v_idx = v_idx, u_idx
        _, idx = self.st_rmq.query(u_idx, v_idx + 1)
        return self.euler_tour[idx]

    def dist(self, u, v):
        lca_uv = self.lca(u, v)
        return self.depth(u) + self.depth(v) - 2 * self.depth(lca_uv)


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

tree = Tree(n, graph, 0)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    ans = tree.dist(a, b) + 1
    print(ans)
