from heapq import heappush, heappop


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


n, m, s = map(int, input().split())

MAX_SILVER = 5005
n2 = MAX_SILVER * n
graph = [[] for _ in range(n2)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    for k in range(a, MAX_SILVER):
        graph[u * MAX_SILVER + k].append((b, v * MAX_SILVER + k - a))
        graph[v * MAX_SILVER + k].append((b, u * MAX_SILVER + k - a))
for i in range(n):
    c, d = map(int, input().split())
    for k in range(MAX_SILVER - 1):
        graph[i * MAX_SILVER + k].append(
            (d, i * MAX_SILVER + min(k + c, MAX_SILVER - 1)))

dist = dijkstra(graph, n2, 0 + min(s, MAX_SILVER - 1))

for i in range(1, n):
    ans_i = 10**20
    for k in range(MAX_SILVER):
        ans_i = min(ans_i, dist[i * MAX_SILVER + k])
    print(ans_i)
