import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


class Tree():
    def __init__(self, n, graph, v_root):
        self.n = n  # number of nodes
        self.graph = graph  # adjacent list of graph
        self.v_root = v_root  # root node

        self.depth = [0] * self.n

        self.init()

    def init(self):
        self.dfs(self.v_root, -1, 0)

    def dfs(self, v, v_par, depth):
        self.depth[v] = depth
        for v_next in self.graph[v]:
            if v_next == v_par:
                continue
            self.dfs(v_next, v, depth + 1)


n = int(input())
graph = [[] for _ in range(n)]
ab = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    ab.append((a, b))

v_root = 0
tree = Tree(n, graph, v_root)
imos = [0] * n
ans = [0] * n

q = int(input())
for _ in range(q):
    t, e, x = map(int, input().split())
    e -= 1
    a, b = ab[e]
    if t == 2:
        a, b = b, a

    if tree.depth[a] < tree.depth[b]:
        imos[v_root] += x
        imos[b] -= x
    else:
        imos[a] += x


def dfs(v, v_par):
    ans[v] += imos[v]
    for v_chi in graph[v]:
        if v_chi == v_par:
            continue
        imos[v_chi] += imos[v]
        dfs(v_chi, v)


# print(ans)
# print(imos)
dfs(v_root, -1)
print(*ans, sep='\n')
