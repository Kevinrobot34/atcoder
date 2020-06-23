h, w = map(int, input().split())
c = [tuple(map(int, input().split())) for _ in range(h)]

c1_cs = [[0] * (w + 1) for _ in range(h + 1)]
c2_cs = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        if (i + j) % 2 == 0:
            c1_cs[i + 1][j + 1] = \
                c1_cs[i + 1][j] + c1_cs[i][j + 1] - c1_cs[i][j] + c[i][j]
            c2_cs[i + 1][j + 1] = \
                c2_cs[i + 1][j] + c2_cs[i][j + 1] - c2_cs[i][j]
        else:
            c1_cs[i + 1][j + 1] = \
                c1_cs[i + 1][j] + c1_cs[i][j + 1] - c1_cs[i][j]
            c2_cs[i + 1][j + 1] = \
                c2_cs[i + 1][j] + c2_cs[i][j + 1] - c2_cs[i][j] + c[i][j]

ans = 0
for i1 in range(h):
    for j1 in range(w):
        for i2 in range(i1 + 1, h + 1):
            for j2 in range(j1 + 1, w + 1):
                s1 = \
                    c1_cs[i2][j2] - c1_cs[i1][j2] - c1_cs[i2][j1] + c1_cs[i1][j1]
                s2 = \
                    c2_cs[i2][j2] - c2_cs[i1][j2] - c2_cs[i2][j1] + c2_cs[i1][j1]
                if s1 == s2:
                    ans = max(ans, (i2 - i1) * (j2 - j1))

print(ans)
