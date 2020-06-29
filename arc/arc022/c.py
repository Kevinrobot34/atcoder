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

ele_id = 0
# dp[v][i] = (頂点vから出るi番目の有向辺に関する部分木のDPの値)
# dp[v][i] = (部分木の深さ)
dp = [[ele_id] * len(graph[i]) for i in range(n)]
ans = [ele_id] * n

add_func = lambda x: x + 1
merge_func = lambda a, b: max(a, b)


def dfs1(v, v_p):
    dp_cum = ele_id
    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            continue
        dp[v][i] = dfs1(v_next, v)
        dp_cum = merge_func(dp_cum, dp[v][i])
    return add_func(dp_cum)


def dfs2(v, v_p, dp_vp):
    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            dp[v][i] = dp_vp
            break

    dp_l = [ele_id] * (len(graph[v]) + 1)
    dp_r = [ele_id] * (len(graph[v]) + 1)
    for i in range(len(graph[v])):
        dp_l[i + 1] = merge_func(dp_l[i], dp[v][i])
    for i in reversed(range(len(graph[v]))):
        dp_r[i] = merge_func(dp_r[i + 1], dp[v][i])

    ans[v] = add_func(dp_l[-1])

    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            continue
        dfs2(v_next, v, add_func(merge_func(dp_l[i], dp_r[i + 1])))


dfs1(0, -1)
dfs2(0, -1, ele_id)

diameter = max(ans)
ans0 = -1
for i in range(n):
    if ans[i] == diameter:
        ans0 = i
        break

depth = [0] * n


def dfs3(v, v_p, d):
    depth[v] = d
    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            continue
        dfs3(v_next, v, d + 1)


dfs3(ans0, -1, 1)
ans1 = -1
for i in range(n):
    if depth[i] == diameter:
        ans1 = i
        break

# print(*ans)
# print(diameter)
print(ans0 + 1, ans1 + 1)
