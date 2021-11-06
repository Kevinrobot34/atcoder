from heapq import heapify, heappop, heappush


def topological_sort(graph: list, n_v: int) -> list:
    # graph[node] = [to1, to2, ...]
    indegree = [0] * n_v  # 各頂点の入次数
    for i in range(n_v):
        for v in graph[i]:
            indegree[v] += 1

    cand = [i for i in range(n_v) if indegree[i] == 0]
    heapify(cand)

    res = []
    while cand:
        v1 = heappop(cand)
        res.append(v1)
        for v2 in graph[v1]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                heappush(cand, v2)

    return res


def is_dag(graph: list, n_v: int):
    ts = topological_sort(graph, n_v)
    return len(ts) == n_v


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append(bi)

ts = topological_sort(graph, n)

if len(ts) != n:
    print(-1)
else:
    print(*[tsi + 1 for tsi in ts])
