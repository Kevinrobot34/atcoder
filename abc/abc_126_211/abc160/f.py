import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

MOD = 10**9 + 7
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

MAX = n + 5
fact = [1] * (MAX + 1)  # i!
finv = [1] * (MAX + 1)  # (i!)^{-1}
iinv = [1] * (MAX + 1)  # i^{-1}
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD

ele_id = (1, 0)
# dp[v][i] = (頂点vから出るi番目の有向辺に関する部分木のDPの値)
# dp[v][i] = (c, m)
# c = 頂点vから出るi番目の有向辺に関する部分木の塗り方の数
# m = 頂点vから出るi番目の有向辺に関する部分木の頂点数
dp = [[ele_id] * len(graph[i]) for i in range(n)]
ans = [ele_id] * n

add_func = lambda x: (x[0], x[1] + 1)


def merge_func(a, b):
    m = a[1] + b[1]
    dp_a = a[0] * finv[a[1]] % MOD
    dp_b = b[0] * finv[b[1]] % MOD
    c = (dp_a * dp_b % MOD) * fact[m] % MOD
    return (c, m)


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
for ans_i, _ in ans:
    print(ans_i)
