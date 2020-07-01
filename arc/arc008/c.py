import sys
input = sys.stdin.readline

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]


def dijkstra(edge_adj: list, node: int, start: int, inf=float('inf')) -> list:
    dist = [inf] * node
    used = [False] * node

    dist[start] = 0
    while True:
        v = -1
        for i in range(node):
            if not used[i] and (v == -1 or dist[v] > dist[i]):
                v = i

        if v == -1:
            break

        used[v] = True
        for i in range(node):
            if dist[i] > dist[v] + edge_adj[v][i]:
                dist[i] = dist[v] + edge_adj[v][i]

    return dist


INF = float('inf')
edge_adj = [[INF] * n for _ in range(n)]
for i, (xi, yi, ti, ri) in enumerate(people):
    for j, (xj, yj, tj, rj) in enumerate(people):
        if i == j:
            continue

        dist = ((xi - xj)**2 + (yi - yj)**2)**0.5
        # i->j
        edge_adj[i][j] = dist / min(ti, rj)
        edge_adj[j][i] = dist / min(tj, ri)

time = dijkstra(edge_adj, n, 0, INF)

ans = 0
time.sort(reverse=True)
# print(time)
for i in range(n - 1):
    ans = max(ans, time[i] + i)

print(ans)
