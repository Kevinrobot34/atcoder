h, w, x, y = map(int, input().split())
s = ['#' * (w + 2)] + [f'#{input()}#' for _ in range(h)] + ['#' * (w + 2)]
di = [+1, 0, -1, 0]
dj = [0, +1, 0, -1]
ans = 1
for k in range(4):
    nx, ny = x, y
    while True:
        nx += di[k]
        ny += dj[k]
        if s[nx][ny] == '.':
            ans += 1
        else:
            break
print(ans)
