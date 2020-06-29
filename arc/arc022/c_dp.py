import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, v_p):
    dist, u, w = 0, v, v
    for v_next in graph[v]:
        if v_next == v_p:
            continue
        dist_i, u_i, w_i = dfs(v_next, v)

    return (d1, l1), (d2, l2)


(_, ans0), (_, ans1) = dfs(0, -1)
ans0 += 1
ans1 += 1
print(dfs(0, -1))
print(ans0, ans1)
