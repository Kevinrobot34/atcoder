import sys
input = sys.stdin.readline

INF = 10**9 + 5
n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

dp = [INF] * n
# dp[i] = (iまでの最小の金の値段)
for v in range(n):
    for v_next in graph[v]:
        dp[v_next] = min(dp[v_next], dp[v], a[v])

ans = max(a[i] - dp[i] for i in range(n) if dp[i] != INF)
print(ans)
