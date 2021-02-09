from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
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
MOD = 28
n2 = n * MOD
graph = [[] for _ in range(n2)]
for _ in range(m):
    fi, ti, ci = map(int, input().split())
    for j in range(MOD):
        if fi != n - 1:
            graph[fi * MOD + j].append((ci, ti * MOD + (j + ci) % MOD))
        if ti != n - 1:
            graph[ti * MOD + j].append((ci, fi * MOD + (j + ci) % MOD))

dist = dijkstra(graph, n2, 0)
ans = min(dist[(n - 1) * MOD + i] for i in range(MOD)
          if i % 4 == 0 or i % 7 == 0)
print(ans)
