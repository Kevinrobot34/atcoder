a = [list(map(int, input().split())) for _ in range(4)]
dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]


def check():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if ni < 0 or nj < 0 or ni > 3 or nj > 3:
                    continue

                if a[i][j] == a[ni][nj]:
                    return False
    return True


ans = 'GAMEOVER' if check() else 'CONTINUE'
print(ans)
