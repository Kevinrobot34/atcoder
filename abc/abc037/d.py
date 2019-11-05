import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
MOD = 10**9 + 7

h, w = map(int, input().split())
a = [[MOD] * (w + 2)] + \
    [[MOD] + list(map(int, input().split())) + [MOD] for _ in range(h)] + \
    [[MOD] * (w + 2)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = [[-1] * (w + 2) for _ in range(h + 2)]


def dfs(i, j):
    if cnt[i][j] != -1:
        return cnt[i][j]

    ans = 1
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if a[i][j] > a[ni][nj]:
            ans += dfs(ni, nj)
            ans %= MOD
    cnt[i][j] = ans
    return ans


ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        ans += dfs(i, j)
        ans %= MOD

print(ans)
