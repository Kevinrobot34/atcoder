import sys
from heapq import heappush, heappop
INF = 10**10
sys.setrecursionlimit(10**8)


def dijkstra(graph: list, n: int, v_s: int, INF: int = INF) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n

    dist[v_s] = 0
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        dist2v, v_from = heappop(heap)
        if dist[v_from] < dist2v:
            continue
        for cost, v_to in graph[v_from]:
            dist_cand = dist2v + cost
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                heappush(heap, (dist[v_to], v_to))
    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
ans = [INF] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        ans[a] = min(c, ans[a])
        continue

    graph[a].append((c, b))

dist = [dijkstra(graph, n, i) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans[i] = min(ans[i], dist[i][j] + dist[j][i])
    if ans[i] == INF:
        ans[i] = -1

print(*ans, sep='\n')
