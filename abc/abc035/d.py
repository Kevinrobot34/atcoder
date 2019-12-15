from heapq import heappush, heappop


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


n, m, t = map(int, input().split())
money = list(map(int, input().split()))
graph1 = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph1[a].append((c, b))
    graph2[b].append((c, a))

dist1 = dijkstra(graph1, n, 0)
dist2 = dijkstra(graph2, n, 0)
# print(dist1)
# print(dist2)
ans = max((t - dist1[i] - dist2[i]) * money[i] for i in range(n))

print(ans)
