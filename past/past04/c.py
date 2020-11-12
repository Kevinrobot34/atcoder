n, m = map(int, input().split())
s = [input() for _ in range(n)]

di = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dj = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(9):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if s[ni][nj] == '#':
                ans[i][j] += 1

for ans_i in ans:
    print(''.join(str(ans_ij) for ans_ij in ans_i))
