h, w, k = 10**3, 10**3, 10**6
x1, y1, x2, y2 = 1, 1, h, w
c = ['.' * w for _ in range(h)]

print(h, w, k)
print(x1, y1, x2, y2)
print(*c, sep='\n')
