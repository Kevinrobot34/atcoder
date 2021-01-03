from collections import deque
import sys
input = sys.stdin.readline


def topological_sort(graph: list, n_v: int) -> list:
    # graph[node] = v_to
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
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

tsort = topological_sort(graph, n)
dp = [0] * n

for v in tsort:
    for v_to in graph[v]:
        dp[v_to] = dp[v] + 1

ans = max(dp)
print(ans)
