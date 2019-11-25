n, m = map(int, input().split())

graph1 = [[] for _ in range(n * 3)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph1[u * 3 + 0].append(v * 3 + 1)
    graph1[u * 3 + 1].append(v * 3 + 2)
    graph1[u * 3 + 2].append(v * 3 + 0)

s, t = map(int, input().split())
s -= 1
t -= 1
s = s * 3
t = t * 3

from heapq import heappush, heappop


def dijkstra(graph: list, n: int, start: int, INF: int = float('inf')) -> list:
    # graph[node] = [(cost, to)]
    dist = [INF] * n
    num = [0] * n

    dist[start] = 0
    heap = [(0, start)]
    while heap:
        _, v_from = heappop(heap)
        for v_to in graph[v_from]:
            dist_cand = dist[v_from] + 1
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                heappush(heap, (dist[v_to], v_to))
    return dist
    # dist = [costs to nodes]


INF = 10**10
dist = dijkstra(graph1, n * 3, s, INF=INF)
if dist[t] == INF:
    print(-1)
else:
    print(dist[t] // 3)
