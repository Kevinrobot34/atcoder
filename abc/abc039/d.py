h, w = map(int, input().split())
s = ['#' * (w + 2)] + ['#' + input() + '#' for _ in range(h)] + ['#' * (w + 2)]
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

t = [['.'] * (w + 2) for _ in range(h + 2)]
ans = [['.'] * (w + 2) for _ in range(h + 2)]


def is_possible():
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            cnt = 0
            for k in range(9):
                if s[i + dx[k]][j + dy[k]] == '#':
                    cnt += 1
            if cnt == 9:
                ans[i][j] = '#'
                for k in range(9):
                    t[i + dx[k]][j + dy[k]] = '#'

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if s[i][j] != t[i][j]:
                return False
    return True


if is_possible():
    print("possible")
    for i in range(1, h + 1):
        print(''.join(ans[i][1:-1]))
else:
    print("impossible")
