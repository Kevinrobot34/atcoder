from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
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


n, m, r, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((c, b))
    graph[b].append((c, a))

ans = 0
for i in range(n):
    dist = dijkstra(graph, n, i, INF=10**9)
    dist.sort()
    # print(i, dist, ans)
    for j in range(1, n):
        x = (dist[j] * t + r - 1) // r
        idx = bisect_left(dist, x)
        # print(j, x, idx)
        if idx > j:
            ans += idx - 2
        else:
            ans += idx - 1

print(ans)
