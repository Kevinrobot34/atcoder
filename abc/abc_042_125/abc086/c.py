n = int(input())

t_prev = x_prev = y_prev = 0
possible = True
for i in range(n):
    t, x, y = map(int, input().split())

    z = (t - t_prev) - (abs(x - x_prev) + abs(y - y_prev))
    if z < 0 or z % 2 == 1:
        possible = False

    t_prev, x_prev, y_prev = t, x, y

if possible:
    print("Yes")
else:
    print("No")
