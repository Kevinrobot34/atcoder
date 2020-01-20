h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

op = []
for j in range(w):
    for i in range(h-1):
        if a[i][j] % 2 == 1:
            a[i][j] -= 1
            a[i+1][j] += 1
            op.append((i, j, i+1, j))

for j in range(w-1):
    if a[h-1][j] % 2 == 1:
        a[h-1][j] -=1
        a[h-1][j+1] +=1
        op.append((h-1, j, h-1, j+1))

print(len(op))
for y1, x1, y2, x2 in op:
    print(y1+1, x1+1, y2+1, x2+1)
