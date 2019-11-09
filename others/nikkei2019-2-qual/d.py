from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(graph: list, node: int, start: int) -> list:
    # graph[node] = [(cost, to)]
    INF = float('inf')
    dist = [INF] * node

    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, thisNode = heappop(heap)
        for NextCost, NextNode in graph[thisNode]:
            dist_cand = dist[thisNode] + NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap, (dist[NextNode], NextNode))
    return dist
    # dist = [costs to nodes]


n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    l, r, c = map(int, input().split())
    l -= 1
    r -= 1
    edge[l].append((c, r))
for i in range(1, n):
    edge[i].append((0, i - 1))

dist = dijkstra(edge, n, 0)
ans = dist[-1] if dist[-1] != float("inf") else -1

print(ans)
