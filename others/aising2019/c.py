import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = [input() for _ in range(h)]

is_used = [[False] * w for _ in range(h)]

di = [+1, 0, -1, 0]
dj = [0, +1, 0, -1]


def dfs(i, j):
    if s[i][j] == '#':
        cnt_w, cnt_b = 0, 1
    else:
        cnt_w, cnt_b = 1, 0

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if is_used[ni][nj]:
            continue
        if s[i][j] == s[ni][nj]:
            continue

        is_used[ni][nj] = True
        cw, cb = dfs(ni, nj)
        cnt_w += cw
        cnt_b += cb
    return (cnt_w, cnt_b)


ans = 0
for i in range(h):
    for j in range(w):
        if not is_used[i][j]:
            is_used[i][j] = True
            cnt_w, cnt_b = dfs(i, j)
            ans += cnt_w * cnt_b

print(ans)
