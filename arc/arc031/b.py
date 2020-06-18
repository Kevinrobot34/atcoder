import sys
sys.setrecursionlimit(10**8)
MAP_SIZE = 10
dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]


def count_island(b):
    def dfs(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= MAP_SIZE or ny < 0 or ny >= MAP_SIZE:
                continue
            if b[nx][ny] == 'o':
                b[nx][ny] = 'x'
                dfs(nx, ny)

    cnt = 0
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if b[i][j] == 'o':
                b[i][j] = 'x'
                dfs(i, j)
                cnt += 1
    return cnt


def check(a):
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if a[i][j] == 'x':
                b = [list(a[k]) for k in range(MAP_SIZE)]
                b[i][j] = 'o'
                cnt = count_island(b)
                # print(i, j, cnt)
                if cnt == 1:
                    return True
    return False


a = [input() for _ in range(MAP_SIZE)]

ans = 'YES' if check(a) else 'NO'
print(ans)
