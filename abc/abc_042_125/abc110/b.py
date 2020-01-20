n, m, x0, y0 = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_max = max(x)
y_min = min(y)

if x_max < y_min:
    if x0 < y_min and x_max < y0:
        print("No War")
    else:
        print("War")
else:
    print("War")
