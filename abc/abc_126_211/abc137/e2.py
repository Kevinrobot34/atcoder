import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, p = map(int, input().split())
edge = []
edge_inv = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a, b, -c+p))
    edge_inv[b].append(a)


visited = [0] * n
def dfs(v):
    for u in edge_inv[v]:
        if visited[u] == 0:
            visited[u] = 1
            dfs(u)

visited[n-1] = 1
dfs(n-1)
target_nodes = set([i for i in range(n) if visited[i] == 1])

INF = float('inf')
d = [INF] * n
d[0] = 0
for i in range(n):
    update = False
    for v_from, v_to, cost in edge:
        if v_from not in target_nodes or v_to not in target_nodes:
            continue
        if d[v_from] != INF and d[v_to] > d[v_from] + cost:
            update = True
            d[v_to] = d[v_from] + cost


if update:
    print(-1)
else:
    print(max(0, -d[n-1]))
