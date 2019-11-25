from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n

    dist[v_s] = 0
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        _, v_from = heappop(heap)
        for cost, v_to in graph[v_from]:
            dist_cand = dist[v_from] + cost
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                heappush(heap, (dist[v_to], v_to))
    return dist


n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    l, r, c = map(int, input().split())
    l -= 1
    r -= 1
    edge[l].append((c, r))
for i in range(1, n):
    edge[i].append((0, i - 1))

INF = 10**15
dist = dijkstra(edge, n, 0, INF=INF)
ans = dist[-1] if dist[-1] != INF else -1

print(ans)
