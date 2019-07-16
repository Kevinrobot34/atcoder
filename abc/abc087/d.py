from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph:list, node:int, start:int) -> list:
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

from collections import deque
def topological_sort(graph: list, n_v: int) -> list:
    res = []
    indegree = [0] * n_v

    for i in range(n_v):
        for c, v in graph[i]:
            indegree[v] += 1

    cand = deque()
    for i in range(n_v):
        if indegree[i] == 0:
            cand.append(i)

    while cand:
        v1 = cand.popleft()
        res.append(v1)
        for c, v2 in graph[v1]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                cand.append(v2)

    return res


def is_dag(graph: list, n_v: int):
    ts = topological_sort(graph, n_v)
    return len(ts) == n_v


n, m = map(int, input().split())
graph = defaultdict(list)
graph2 = defaultdict(list)
edges = []
l_nodes = set()
r_nodes = set()
for i in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    edges.append((l, r, d))
    graph[l].append((d, r))
    graph2[r].append((d, l))

    l_nodes.add(l)
    r_nodes.add(r)


if m == 0:
    print("Yes")
elif not is_dag(graph, n):
    print("No")
else:
    x = l_nodes - r_nodes

    dist = dijkstra(graph, n, list(x)[0])
    possible = True
    for l, r, d in edges:
        if dist[l] != float('inf') and dist[r] != float('inf') and d != abs(dist[l] - dist[r]):
            possible = False
            break

    if possible:
        x = r_nodes - l_nodes

        dist = dijkstra(graph2, n, list(x)[0])
        possible = True
        for l, r, d in edges:
            if dist[l] != float('inf') and dist[r] != float('inf') and d != abs(dist[l] - dist[r]):
                possible = False
                break
        if possible:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
