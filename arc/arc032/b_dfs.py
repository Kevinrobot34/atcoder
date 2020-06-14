import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

is_visited = [False] * n


def dfs(v):
    for v_next in graph[v]:
        if not is_visited[v_next]:
            is_visited[v_next] = True
            dfs(v_next)


ans = 0
for i in range(n):
    if not is_visited[i]:
        ans += 1
        is_visited[i] = True
        dfs(i)
ans -= 1
print(ans)
