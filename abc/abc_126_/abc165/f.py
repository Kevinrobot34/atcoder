import sys
from copy import copy
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
INF = float('inf')

n = int(input())
a = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

ans = [0] * n
dp = [INF] * n
dp[0] = a[0]
# dp[i] = (長さi+1の増加部分列の最終項のmin)


def dfs(v, v_p):
    ans[v] = bisect_left(dp, INF)

    for v_next in graph[v]:
        if v_next == v_p:
            continue

        idx = bisect_left(dp, a[v_next])
        past = dp[idx]
        dp[idx] = a[v_next]
        dfs(v_next, v)
        dp[idx] = past


dfs(0, -1)
print(*ans, sep='\n')
