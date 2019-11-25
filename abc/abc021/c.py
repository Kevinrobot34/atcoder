from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(graph: list,
             n: int,
             v_s: int,
             INF: int = float('inf'),
             MOD: int = 10**9 + 7) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n
    num = [0] * n

    dist[v_s] = 0
    num[v_s] = 1
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        _, v_from = heappop(heap)
        for v_to in graph[v_from]:
            dist_cand = dist[v_from] + 1
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                num[v_to] = num[v_from]
                heappush(heap, (dist[v_to], v_to))
            elif dist_cand == dist[v_to]:
                num[v_to] += num[v_from]
                num[v_to] %= MOD
    return dist, num


n = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
graph = [[] for _ in range(n)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

dist, num = dijkstra(graph, n, a, INF=10**10, MOD=10**9 + 7)

print(num[b])
