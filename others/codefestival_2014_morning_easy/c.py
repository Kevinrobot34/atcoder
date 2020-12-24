from heapq import heappush, heappop
INF = float('inf')


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
s, t = map(lambda x: int(x) - 1, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append((d, y))
    graph[y].append((d, x))

dist_s = dijkstra(graph, n, s, INF)
dist_t = dijkstra(graph, n, t, INF)

ans = -1
for i in range(n):
    if i == s or i == t:
        continue
    if dist_s[i] == INF or dist_t[i] == INF:
        continue
    if dist_s[i] == dist_t[i]:
        ans = i + 1
        break
print(ans)
