import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
c = list(map(lambda x: int(x) - 1, input().split()))

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ans = [n * (n + 1) // 2] * n
n_subtree = [1] * n  # n_st[i] = (頂点iの部分木の頂点数)
cnt = [0] * n  # cnt[i] = (訪問済み頂点のうち、色iを通過しないとたどり着けない頂点数)
n_visited = 0


def dfs(v, v_p):
    global n_visited
    cnt_v_before = cnt[c[v]]
    for v_next in graph[v]:
        if v_next == v_p:
            continue

        m_prev = n_visited - cnt[c[v]]
        dfs(v_next, v)
        n_subtree[v] += n_subtree[v_next]
        m_next = n_visited - cnt[c[v]]

        m = m_next - m_prev
        ans[c[v]] -= m * (m + 1) // 2

    cnt[c[v]] = cnt_v_before + n_subtree[v]
    n_visited += 1


dfs(0, -1)

for i in range(n):
    m = n - cnt[i]
    ans[i] -= m * (m + 1) // 2

print(*ans, sep='\n')
