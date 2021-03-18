import sys
from heapq import heappop, heappush


def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n

    dist[v_s] = 0
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        dist2v, v_from = heappop(heap)
        if dist[v_from] < dist2v:
            continue
        for (t, k), v_to in graph[v_from]:
            dist_cand = ((dist2v + k - 1) // k) * k + t
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                heappush(heap, (dist[v_to], v_to))
    return dist


input = sys.stdin.readline
INF = float('inf')
n, m, x, y = map(int, input().split())
x -= 1
y -= 1
graph = [[] for _ in range(n)]
for _ in range(m):
    ai, bi, ti, ki = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append(((ti, ki), bi))
    graph[bi].append(((ti, ki), ai))

dist = dijkstra(graph, n, x, INF)
ans = -1 if dist[y] == INF else dist[y]
print(ans)
