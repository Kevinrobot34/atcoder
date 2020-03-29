n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
ds = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        ds[i + 1][j + 1] = ds[i + 1][j] + ds[i][j + 1] - ds[i][j] + d[i][j]


def f(i1, j1, i2, j2):
    return ds[i2][j2] - ds[i1][j2] - ds[i2][j1] + ds[i1][j1]


cnt = [0] * (n**2 + 1)
cnt_max = [0] * (n**2 + 1)
for i1 in range(n):
    for j1 in range(n):
        for i2 in range(i1 + 1, n + 1):
            for j2 in range(j1 + 1, n + 1):
                a = (i2 - i1) * (j2 - j1)
                cnt[a] = max(cnt[a], f(i1, j1, i2, j2))

for i in range(1, n**2 + 1):
    cnt_max[i] = max(cnt[i], cnt_max[i - 1])

ans = 0
q = int(input())
for _ in range(q):
    p = int(input())
    print(cnt_max[p])
