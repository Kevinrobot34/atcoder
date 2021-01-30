from collections import deque
import sys
input = sys.stdin.readline
INF = 10**8

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append(bi)
    graph[bi].append(ai)
k = int(input())
c = list(map(lambda x: int(x) - 1, input().split()))


def bfs(v_start):
    dist = [INF] * n
    dist[v_start] = 0
    queue = deque([(v_start, 0)])
    while queue:
        v, cost = queue.popleft()
        for v_to in graph[v]:
            if dist[v_to] != INF:
                continue
            queue.append((v_to, cost + 1))
            dist[v_to] = cost + 1
    return dist


graph_adj = [[INF] * (k + 1) for _ in range(k + 1)]
for i, ci in enumerate(c):
    dist = bfs(ci)
    for j, cj in enumerate(c):
        if i == j:
            continue
        graph_adj[i][j] = graph_adj[j][i] = dist[cj]
# print(*graph_adj, sep='\n')

dp = [[INF] * (1 << k) for _ in range(k)]
# dp[i][bit] = bitに訪問済みの状態で頂点iにいる時の最小コスト
for i in range(k):
    dp[i][1 << i] = 1
for bit in range(1, 1 << k):
    for i in range(k):
        if (bit >> i) & 1:
            continue
        dp[i][bit | (1 << i)] = min(
            dp[i][bit | (1 << i)],
            min(dp[j][bit] + graph_adj[j][i] for j in range(k)))

# print(*dp, sep='\n')
ans = min(dp[i][(1 << k) - 1] for i in range(k))
if ans == INF:
    ans = -1
print(ans)
