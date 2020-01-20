import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
edge = []
edge_inv = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edge.append((a, b, -c))
    edge_inv[b].append(a)

visited = [False] * n
def dfs(v):
    for u in edge_inv[v]:
        if not visited[u]:
            visited[u] = True
            dfs(u)

visited[n-1] = True
dfs(n-1)
target_nodes = [i for i in range(n) if visited[i]]
# print(target_nodes)

def bellman_ford(n, edge):
    INF = float('inf')
    d = [INF] * n
    d[0] = 0
    for i in range(n):
        update = False
        for v_from, v_to, cost in edge:
            if v_from not in target_nodes or v_to not in target_nodes:
                continue
            if d[v_from] != INF and d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost # 緩和
                update = True
    return d, update

d, update = bellman_ford(n, edge)
if update:
    print("inf")
else:
    print(-d[n-1])
