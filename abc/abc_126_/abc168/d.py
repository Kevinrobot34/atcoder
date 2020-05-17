from heapq import heappush, heappop


def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n
    prev_node = [-1] * n

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
                prev_node[v_to] = v_from
                heappush(heap, (dist[v_to], v_to))
    return dist, prev_node


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((1, b))
    graph[b].append((1, a))

dist, prev_node = dijkstra(graph, n, 0)
# print(dist)
# print(prev_node)

print('Yes')
for i in range(1, n):
    print(prev_node[i] + 1)
