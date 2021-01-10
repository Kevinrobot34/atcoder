import sys
from collections import deque
from operator import itemgetter
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
ia = list(enumerate(a))
ia.sort(key=itemgetter(1))
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

is_visited = [False] * n


def bfs(v_start):
    queue = deque([v_start])
    p_max = -float('inf')
    while queue:
        v = queue.popleft()
        for v_next in graph[v]:
            if is_visited[v_next]:
                continue
            queue.append(v_next)
            is_visited[v_next] = True
            p_max = max(p_max, a[v_next])

    return p_max - a[v_start]


ans = max([bfs(i) for i, _ in ia if not is_visited[i]])
print(ans)
