h, w = map(int, input().split())
s = ['#' * (w + 2)] + ['#' + input() + '#' for _ in range(h)] + ['#' * (w + 2)]
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]


def is_possible():
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            cnt = 0
            for k in range(9):
                if s[i + dx[k]][j + dy[k]] == '#':
                    cnt += 1
            if 1 <= cnt <= 8:
                return False

    return True


ans = "possible" if is_possible() else "impossible"

print(ans)
