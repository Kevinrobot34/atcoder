h, w = map(int, input().split())

mm = ['#' + input() + '#' for i in range(h)]
m = ['#' * (w+2)] + mm + ['#' * (w+2)]

# for i in range(h+2):
#     print(m[i])

#vertical = [[0] * (w+1) for i in range(h+1)]
vertical = [[0], ]
for i in range(1, h+1):
    c = 0
    tmp = [0]
    for j in range(1, w+2):
        if m[i][j] == '#':
            tmp.extend([j-c-1] * (j-c-1))
            tmp.append(0)
            c = j
    vertical.append(tmp)

# for i in range(1, h+1):
#     print(vertical[i])

#horizontal = [[0] * (w+1) for i in range(h+1)]
horizontal = [[0], ]
for i in range(1, w+1):
    c = 0
    tmp = [0]
    for j in range(1, h+2):
        if m[j][i] == '#':
            tmp.extend([j-c-1] * (j-c-1))
            tmp.append(0)
            c = j
    horizontal.append(tmp)

# for i in range(1, w+1):
#     print(horizontal[i])

ans = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        ans = max(ans, vertical[i][j] + horizontal[j][i] - 1)

print(ans)
