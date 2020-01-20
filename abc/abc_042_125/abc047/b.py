w, h, n = map(int, input().split())
c = [[0] * w for _ in range(h)]

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(h):
            for j in range(x):
                c[i][j] = 1
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                c[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(w):
                c[i][j] = 1
    elif a == 4:
        for i in range(y, h):
            for j in range(w):
                c[i][j] = 1

ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == 0:
            ans += 1

print(ans)
