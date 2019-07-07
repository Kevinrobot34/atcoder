n, m = map(int, input().split())

graph1 = [[] for _ in range(n*3)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph1[u*3+0].append(v*3+1)
    graph1[u*3+1].append(v*3+2)
    graph1[u*3+2].append(v*3+0)

s, t = map(int, input().split())
s -= 1
t -= 1
s = s*3
t = t*3

from heapq import heappush, heappop
def dijkstra(graph:list, node:int, start:int) -> list:
    # graph[node] = [(cost, to)]
    inf = float('inf')
    dist = [inf] * node

    dist[start] = 0
    heap = [(0, start)]
    NextCost = 1
    while heap:
        cost, thisNode = heappop(heap)
        for NextNode in graph[thisNode]:
            dist_cand = dist[thisNode] + NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap, (dist[NextNode], NextNode))
    return dist
    # dist = [costs to nodes]

inf = float('inf')
dist = dijkstra(graph1, n*3, s)
if dist[t] == inf:
    print(-1)
else:
    print(dist[t]//3)
