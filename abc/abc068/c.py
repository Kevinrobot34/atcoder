from heapq import heappush, heappop
def dijkstra(graph: list, node: int, start: int) -> list:
    # graph[node] = [(cost, to)]
    inf = float('inf')
    dist = [inf] * node

    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, thisNode = heappop(heap)
        for NextCost, NextNode in graph[thisNode]:
            dist_cand = dist[thisNode] + NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap,(dist[NextNode], NextNode))
    return dist
    # dist = [costs to nodes]

n, m = map(int, input().split())
edge = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((1, b))
    edge[b].append((1, a))

dist = dijkstra(edge, n, 0)
if dist[n-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
