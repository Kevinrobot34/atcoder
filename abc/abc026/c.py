n = int(input())
edge = [[] for _ in range(n)]
for i in range(1, n):
    b = int(input())
    b -= 1
    edge[b].append(i)
    edge[i].append(b)

salary = [-1] * n
def dfs(v, p):
    if p != -1 and len(edge[v]) == 1:
        return 1

    x = []
    for u in edge[v]:
        if u != p:
            x.append(dfs(u, v))

    # print(v, p, max(x) + min(x) + 1)
    return max(x) + min(x) + 1

ans = dfs(0, -1)
print(ans)
