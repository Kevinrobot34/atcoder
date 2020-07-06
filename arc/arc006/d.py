import sys
sys.setrecursionlimit(2 * 10**9)

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
di = [-1, 0, +1, -1, +1, -1, 0, +1]
dj = [-1, -1, -1, 0, 0, +1, +1, +1]


def dfs(i0, j0):
    global c
    cnt = 1
    queue = [(i0, j0)]
    c[i0][j0] = '.'
    while queue:
        i, j = queue.pop()

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if c[ni][nj] == 'o':
                c[ni][nj] = '.'
                cnt += 1
                queue.append((ni, nj))
    return cnt


ans = [0, 0, 0]

for i in range(h):
    for j in range(w):
        if c[i][j] == 'o':
            cnt = dfs(i, j)
            x = 2
            while x**2 <= cnt:
                while cnt % (x**2) == 0:
                    cnt //= (x**2)
                x += 1
            # print(cnt)
            if cnt == 3:
                ans[0] += 1  # A
            elif cnt == 1:
                ans[1] += 1  # B
            elif cnt == 11:
                ans[2] += 1  # C

print(*ans)
