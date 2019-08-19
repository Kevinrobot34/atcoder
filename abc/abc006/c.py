n, m = map(int, input().split())

x = y = z = 0
if 4*n - m < 0:
    x, y, z = -1, -1, -1
else:
    x = 0
    while True:
        y = 4*n - m - 2*x
        z = n - x - y
        if y < 0 or z >= 0:
            break
        else:
            x += 1
    if y < 0:
        x, y, z = -1, -1, -1

print(x, y, z)
