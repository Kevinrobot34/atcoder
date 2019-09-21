def kmp(s):
    n = len(s)
    kmp = [0] * (n+1)
    kmp[0] = -1
    j = -1
    for i in range(n):
        while j >= 0 and s[i] != s[j]:
            j = kmp[j]
        j += 1
        kmp[i+1] = j

    return kmp

from collections import deque
def topological_sort(graph: list, n_v: int) -> list:
    # graph[node] = [(cost, to)]
    indegree = [0] * n_v # 各頂点の入次数
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

import sys

def main():
    input = sys.stdin.readline
    s = input().rstrip()
    t = input().rstrip()

    n0 = len(s)
    m = len(t)

    s = s * (m // n0 + 2)

    res = kmp(t + '*' + s)
    res = res[m+2:]

    graph = [set() for _ in range(n0)]
    for i in range(len(res)):
        if res[i] >= m:
            graph[(i-m+1)%n0].add( (i + 1) % n0 )
    # print(graph)

    ts = topological_sort(graph, n0)
    if len(ts) != n0:
        ans = -1
    else:
        # print(ts)
        ans = 0
        path = [0] * n0
        for i in range(n0):
            ans = max(ans, path[ts[i]])
            for j in graph[ts[i]]:
                path[j] = path[ts[i]] + 1

    print(ans)

main()
