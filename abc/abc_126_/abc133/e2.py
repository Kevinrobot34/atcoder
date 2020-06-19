import sys
sys.setrecursionlimit(10**9)

MOD = 10**9 + 7
n, k = map(int, input().split())
graph = [[] for _ in range(n)]
k_inv = pow(k, MOD - 2, MOD)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, v_p):
    # 子部分木の塗り方の場合の数
    if v_p == -1:  # root
        c = k - 1
    else:
        c = k - 2

    cnt = 1
    i = 0
    for v_next in graph[v]:
        if v_next == v_p:
            continue
        cnt *= max(0, c - i)
        cnt %= MOD
        cnt *= dfs(v_next, v)
        cnt %= MOD
        i += 1
    return cnt


ans = dfs(0, -1) * k % MOD
print(ans)
