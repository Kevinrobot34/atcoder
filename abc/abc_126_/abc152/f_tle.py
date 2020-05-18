import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


class Tree():
    def __init__(self, n, graph, v_root):
        self.n = n  # number of nodes
        self.graph = graph  # adjacent list of graph
        self.v_root = v_root  # root node

        self.logn = (self.n - 1).bit_length()
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.depth = [0] * self.n
        self.lca_table = [[-1] * self.n for _ in range(n)]

        self.init()

    def init(self):
        self.dfs(self.v_root, -1, 0)
        # doubling
        for k in range(self.logn - 1):
            for v in range(self.n):
                if self.parent[k][v] != -1:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]
        # create lca table
        for i in range(n):
            for j in range(n):
                self.lca_table[i][j] = self.lca(i, j)

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

    def calc(self, cnt, v, v_par, ans):
        ret = cnt[v]
        for v_next in self.graph[v]:
            if v_next == v_par:
                continue
            ans += self.calc(cnt, v_next, v, 0)
            ret += cnt[v_next]
        cnt[v] = ret
        if ret == 0:
            ans += 1
        return ans


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

tree = Tree(n, graph, n // 2)

m = int(input())
cond = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    cond.append((u, v, tree.lca_table[u][v]))

ans = 1 << (n - 1)
for bit in range(1, 1 << m):
    cnt = [0] * n
    l = 0
    for i, (u, v, lca) in enumerate(cond):
        if (bit >> i) & 1:
            cnt[u] += 1
            cnt[v] += 1
            cnt[lca] -= 2
            l += 1

    # print(bin(bit), cnt)
    c = tree.calc(cnt, 0, -1, 0) - 1
    # print(bin(bit), cnt, c, l)
    ans += ((-1)**(l % 2)) * (1 << c)

print(ans)
