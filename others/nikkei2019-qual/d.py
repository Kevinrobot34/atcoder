from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def topological_sort(graph: list, n_v: int) -> list:
    # graph[node] = [to, ]
    indegree = [0] * n_v  # 各頂点の入次数
    for i in range(n_v):
        for v in graph[i]:
            indegree[v] += 1

    cand = deque([i for i in range(n_v) if indegree[i] == 0])
    res = []
    while cand:
        v1 = cand.popleft()
        res.append(v1)
        for v2 in graph[v1]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                cand.append(v2)

    return res


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(n + m - 1):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append(bi)

ts = topological_sort(graph, n)
ans = [-1] * n
for v in ts:
    for v_to in graph[v]:
        ans[v_to] = v

ans = [ans_i + 1 for ans_i in ans]
print(*ans, sep='\n')
