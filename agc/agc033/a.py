h, w = map(int, input().split())
a = ['#' * (w+2)] + ['#' + input() + '#' for i in range(h)] + ['#' * (w+2)]
for i in range(h+2):
    a[i] = list(a[i])

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x = []
for i in range(1, h+1):
    for j in range(1, w+1):
        if a[i][j] == '#':
            x.append((i, j))

ans = 0
while x:
    y = []
    for i, j in x:
        for di, dj in d:
            if a[i+di][j+dj] == '.':
                a[i+di][j+dj] = '#'
                y.append((i+di, j+dj))
    x = y
    ans += 1
    # for i in range(h+2):
    #     print("".join(a[i]))
    # print()

ans -= 1
print(ans)
