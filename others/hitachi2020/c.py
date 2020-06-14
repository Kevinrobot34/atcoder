import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

bigraph = [0] * n


def dfs(v, v_p, depth):
    bigraph[v] = depth % 2
    for v_next in graph[v]:
        if v_next == v_p:
            continue
        dfs(v_next, v, depth + 1)


dfs(0, -1, 1)
m1 = sum(bigraph)
m2 = n - m1

ans = [-1] * n
if m1 > n // 3 and m2 > n // 3:
    c1 = 1
    c2 = 2
    for i in range(n):
        if bigraph[i] == 0 and c1 <= n:
            ans[i] = c1
            c1 += 3
        if bigraph[i] == 1 and c2 <= n:
            ans[i] = c2
            c2 += 3
    c3 = 3
    for i in range(n):
        if ans[i] == -1:
            ans[i] = c3
            c3 += 3
elif m1 > m2:
    # print('A')
    c1 = 1
    c2 = 2
    c3 = 3
    for i in range(n):
        if bigraph[i] == 0:
            # print(i, c1)
            ans[i] = c3
            c3 += 3
    for i in range(n):
        if ans[i] == -1:
            if c1 <= n:
                ans[i] = c1
                c1 += 3
            elif c2 <= n:
                ans[i] = c2
                c2 += 3
            else:
                ans[i] = c3
                c3 += 3
else:  # m1 < m2
    # print('B')
    c1 = 1
    c2 = 2
    c3 = 3
    for i in range(n):
        if bigraph[i] == 1:
            # print(i, c1)
            ans[i] = c3
            c3 += 3
    for i in range(n):
        if ans[i] == -1:
            if c1 <= n:
                ans[i] = c1
                c1 += 3
            elif c2 <= n:
                ans[i] = c2
                c2 += 3
            else:
                ans[i] = c3
                c3 += 3

print(*ans)
