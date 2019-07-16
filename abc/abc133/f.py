from collections import defaultdict
import math
n, q = map(int, input().split())
edge = defaultdict(list)
for i in range(n-1):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c, d))
    edge[b].append((a, c, d))


MAX_LOG_V = math.ceil(math.log2(n)) + 1
print(MAX_LOG_V)
parents = [[0] * MAX_LOG_V for i in range(n)]
depth = [0] * n
def dfs(v, p, d):
    parents[v][0] = p
    depth[v] = d
    for nv, _, _ in edge[v]:
        if nv != p:
            dfs(nv, v, d+1)

dfs(4, -1, 0)
for i in range(1, MAX_LOG_V):
    for v in range(n):
        if parents[v][i-1] == -1:
            parents[v][i] = -1
        else:
            parents[v][i] = parents[parents[v][i-1]][i-1]

for v in range(n):
    print(depth[v], parents[v])


def lca(u: int, v: int) -> int:
    # uとvが同じ深さになるまで、深い方の親をたどる
    if depth[u] > depth[v]:
        u, v = v, u
    for k in range(MAX_LOG_V):
        if ((depth[v] - depth[u]) >> k) & 1 == 1:
            v = parents[v][k]

    # LCAを二分探索
    if u == v:
        return u
    for k in reversed(range(MAX_LOG_V)):
        if parents[u][k] != parents[v][k]:
            u = parents[u][k]
            v = parents[v][k]
    return parents[u][0]
