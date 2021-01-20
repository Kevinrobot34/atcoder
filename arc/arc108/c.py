import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    ui, vi, ci = map(int, input().split())
    ui -= 1
    vi -= 1
    graph[ui].append((ci, vi))
    graph[vi].append((ci, ui))

color = [0] * n


def func(v, v_par):
    for ci, v_to in graph[v]:
        if v_to == v_par:
            continue
        elif color[v_to] != 0:
            continue

        if color[v] == ci:
            color[v_to] = ci % n + 1
        else:
            color[v_to] = ci
        func(v_to, v)


color[0] = 1
func(0, -1)

print(*color, sep='\n')
