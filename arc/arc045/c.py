import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, z = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append((y, c))
    graph[y].append((x, c))

cost_cs = [0] * n


def dfs(v, v_p):
    for v_next, c in graph[v]:
        if v_next == v_p:
            continue
        cost_cs[v_next] = cost_cs[v] ^ c
        dfs(v_next, v)


dfs(0, -1)
cnt = defaultdict(int)
for i in range(n):
    cnt[cost_cs[i]] += 1

ans = 0
for i in range(n):
    # print(i, cost_cs[i], z ^ cost_cs[i], cnt[z ^ cost_cs[i]])
    if z == 0:
        ans += cnt[cost_cs[i]] - 1
    else:
        ans += cnt[z ^ cost_cs[i]]
ans //= 2
print(ans)
