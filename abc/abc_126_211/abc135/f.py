def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n

    i = 1
    lcp = 0
    while i < n:
        while i+lcp < n and s[i+lcp] == s[lcp]:
            lcp += 1
        z[i] = lcp

        if lcp == 0:
            i += 1
            continue

        k = 1
        while i+k < n and k+z[k] < lcp:
            z[i+k] = z[k]
            k += 1
        i += k
        lcp -= k

    return z

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


    z = z_algorithm(t + '*' + s)
    z = z[m+1:]
    # print(z)

    graph = [[] for _ in range(n0)]
    for i in range(n0):
        if z[i] >= m:
            graph[i].append( (i + m) % n0 )
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
