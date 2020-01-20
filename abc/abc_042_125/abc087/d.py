from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(graph: list, n_v: int) -> list:
    # graph[node] = [(cost, to)]
    indegree = [0] * n_v # 各頂点の入次数
    for i in range(n_v):
        for c, v in graph[i]:
            indegree[v] += 1

    cand = deque([i for i in range(n_v) if indegree[i] == 0])
    res = []
    while cand:
        v1 = cand.popleft()
        res.append(v1)
        for c, v2 in graph[v1]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                cand.append(v2)

    return res


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    edges[l].append((d, r))

ts = topological_sort(edges, n)

if len(ts) != n:
    # Not DAG
    ans = "No"
else:
    # DAG
    dist = [-1] * n
    ans = "Yes"
    for v in ts:
        if dist[v] == -1:
            dist[v] = 0

        for c, u in edges[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + c
            elif dist[u] != dist[v] + c:
                ans = "No"
                break

print(ans)
