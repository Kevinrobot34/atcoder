import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]  #[(v_to, edge_idx)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, i))
    graph[b].append((a, i))


def dfs(v, v_p, target):
    if v == target:
        return True, 0

    for v_next, edge_idx in graph[v]:
        if v_next == v_p:
            continue
        is_target, path = dfs(v_next, v, target)
        if is_target:
            return is_target, path | (1 << edge_idx)
    return False, 0


m = int(input())
cond = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    _, path = dfs(u, -1, v)
    # print(u, v, bin(path))
    cond.append((u, v, path))

ans = 1 << (n - 1)
for bit in range(1, 1 << m):
    l = 0
    path = 0
    for i, (u, v, path_i) in enumerate(cond):
        if (bit >> i) & 1:
            l += 1
            path = path | path_i

    c = n - 1 - bin(path).count('1')
    ans += ((-1)**(l % 2)) * (1 << c)

print(ans)
