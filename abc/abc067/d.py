import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
edge = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

d1 = [-1] * n
d2 = [-1] * n
def dfs(v, d):
    for v_next in edge[v]:
        if d[v_next] == -1:
            d[v_next] = d[v] + 1
            dfs(v_next, d)

d1[0] = 0
dfs(0, d1)
d2[-1] = 0
dfs(n-1, d2)

n_f = 0
for i in range(n):
    if d1[i] <= d2[i]:
        n_f += 1

if n_f > n // 2:
    ans = "Fennec"
else:
    ans = "Snuke"
print(ans)
