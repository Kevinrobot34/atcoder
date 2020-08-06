from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
in_degree = [0] * n
out_degree = [0] * n
for _ in range(n - 1 + m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph2[b].append(a)
    in_degree[b] += 1
    out_degree[a] += 1

v_root = in_degree.index(0)

depth = [-1] * n
ans = [0] * n
depth[v_root] = 0


def dfs(v):
    if depth[v] == -1:
        for v_par in graph2[v]:
            d = dfs(v_par)
            if depth[v] < d + 1:
                depth[v] = d + 1
                ans[v] = v_par + 1
    return depth[v]


for i in range(n):
    if out_degree[i] == 0:
        # print(i)
        _ = dfs(i)

print(*ans, sep='\n')
