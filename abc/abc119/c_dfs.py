n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
INF = 10**9

def dfs(index, x, y, z):
    if index == n:
        return abs(a-x) + abs(b-y) + abs(c-z) - 30 if min(x, y, z) > 0 else INF

    cand1 = dfs(index+1, x+l[index], y, z) + 10
    cand2 = dfs(index+1, x, y+l[index], z) + 10
    cand3 = dfs(index+1, x, y, z+l[index]) + 10
    cand4 = dfs(index+1, x, y, z)

    return min(cand1, cand2, cand3, cand4)

print(dfs(0, 0, 0, 0))
