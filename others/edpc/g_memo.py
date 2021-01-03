import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

dp = [-1] * n


def f(v):
    if dp[v] != -1:
        return dp[v]
    dp[v] = 0
    for v_to in graph[v]:
        dp[v] = max(dp[v], f(v_to) + 1)
    return dp[v]


ans = max(f(i) for i in range(n))
print(ans)
