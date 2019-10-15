import sys
input = sys.stdin.readline

def dijkstra(edge_adj: list, node: int, start: int) -> list:
    inf = 3 * 10 ** 9
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
    # dist = [costs to nodes]

xs, ys, xt, yt = map(int, input().split())
n = int(input())
circles = [(xs, ys, 0), (xt, yt, 0)]
for i in range(n):
    circles.append(tuple(map(int, input().split())))
n += 2

edges = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist = ((circles[i][0] - circles[j][0]) ** 2 + (circles[i][1] - circles[j][1]) ** 2) ** 0.5
        cost = max(0, dist - circles[i][2] - circles[j][2])
        edges[i][j] = cost
        edges[j][i] = cost


dist = dijkstra(edges, n, 0)

print(dist[1])
