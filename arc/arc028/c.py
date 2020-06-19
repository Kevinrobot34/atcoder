import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n)]
for i in range(1, n):
    p = int(input())
    graph[i].append(p)
    graph[p].append(i)

# dp[v][i] = (頂点vから出るi番目の有向辺に関する部分木のDPの値)
# dp[v][i] = (a, b)
# a = (頂点vから出るi番目の有向辺に関する部分木の頂点数)
# b = (頂点vから出るi番目の有向辺に関する部分木の子部分木の最大の頂点数)
ele_id = (0, 0)
dp = [[ele_id] * len(graph[i]) for i in range(n)]
ans = [ele_id] * n


def add_func(x):
    a, b = x
    return (a + 1, b)


def preprocess(x):
    a, b = x
    return (a, a)


def merge_func(x1, x2):
    a1, b1 = x1
    a2, b2 = x2
    return (a1 + a2, max(b1, b2))


def dfs1(v, v_p):
    dp_cum = ele_id
    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            continue
        dp[v][i] = dfs1(v_next, v)
        dp_cum = merge_func(dp_cum, preprocess(dp[v][i]))
    return add_func(dp_cum)


def dfs2(v, v_p, dp_vp):
    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            dp[v][i] = dp_vp

    dp_l = [ele_id] * (len(graph[v]) + 1)
    dp_r = [ele_id] * (len(graph[v]) + 1)
    for i in range(len(graph[v])):
        dp_l[i + 1] = merge_func(dp_l[i], preprocess(dp[v][i]))
    for i in reversed(range(len(graph[v]))):
        dp_r[i] = merge_func(dp_r[i + 1], preprocess(dp[v][i]))

    ans[v] = add_func(dp_l[-1])

    for i, v_next in enumerate(graph[v]):
        if v_next == v_p:
            continue
        dfs2(v_next, v, add_func(merge_func(dp_l[i], dp_r[i + 1])))


dfs1(0, -1)
dfs2(0, -1, ele_id)
for _, ans_i in ans:
    print(ans_i)
