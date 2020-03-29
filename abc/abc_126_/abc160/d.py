from heapq import heappush, heappop


def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [v_to, ...]
    dist = [INF] * n

    dist[v_s] = 0
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        _, v_from = heappop(heap)
        for v_to in graph[v_from]:
            dist_cand = dist[v_from] + 1
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                heappush(heap, (dist[v_to], v_to))
    return dist


n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for i in range(n):
    if i - 1 >= 0:
        g[i].append(i - 1)
    if i + 1 < n:
        g[i].append(i + 1)
g[x].append(y)
g[y].append(x)

d = [dijkstra(g, n, i) for i in range(n)]
# print(*d, sep='\n')

ans = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        ans[d[i][j]] += 1

for k in range(1, n):
    print(ans[k])
