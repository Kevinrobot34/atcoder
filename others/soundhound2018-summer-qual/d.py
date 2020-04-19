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


n, m, s, t = map(int, input().split())
s -= 1
t -= 1
g_yen = [[] for _ in range(n)]
g_snu = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    # for yen
    g_yen[u].append((a, v))
    g_yen[v].append((a, u))
    # for snuke
    g_snu[u].append((b, v))
    g_snu[v].append((b, u))

d_yen = dijkstra(g_yen, n, s)
d_snu = dijkstra(g_snu, n, t)

d = [d_yen[i] + d_snu[i] for i in range(n)]

ans = [10**15] * n
ans[n - 1] = d[n - 1]
for i in reversed(range(n - 1)):
    ans[i] = min(ans[i + 1], d[i])

for i in range(n):
    ans[i] = 10**15 - ans[i]

print(*ans, sep='\n')
