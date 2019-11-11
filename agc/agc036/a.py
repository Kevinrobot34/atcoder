s = int(input())

L_MAX = 10**9

x1, y1 = 0, 0
x2, y2 = L_MAX, 1
x3 = ((s + L_MAX - 1) // L_MAX) * L_MAX - s
y3 = (s + L_MAX - 1) // L_MAX

print(x1, y1, x2, y2, x3, y3)
