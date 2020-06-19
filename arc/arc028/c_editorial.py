import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n)]
for i in range(1, n):
    p = int(input())
    graph[i].append(p)
    graph[p].append(i)

# dp[i] = (根付き木として考えたときのi以下の部分木の大きさ)
dp = [0] * n
par = [-1] * n


def dfs(v, v_p):
    # ある根付き木に対し、子部分木のサイズを求めるDFS
    par[v] = v_p
    cnt = 1
    for v_next in graph[v]:
        if v_next == v_p:
            continue
        cnt += dfs(v_next, v)
    dp[v] = cnt
    return cnt


_ = dfs(0, -1)

ans = [0] * n
for i in range(n):
    for v in graph[i]:
        if v == par[i]:
            ans[i] = max(ans[i], n - dp[i])
        else:
            ans[i] = max(ans[i], dp[v])
# print(dp)
print(*ans, sep='\n')
