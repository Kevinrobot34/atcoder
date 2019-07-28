a, b = map(int, input().split())

def func(x):
    if x <= 1:
        return x
    elif x == 2:
        return 3
    elif x == 3:
        return 0

    y = 1
    while y*2 <= x:
        y *= 2

    if (x - y + 1) % 2 == 1:
        return y + func(x - y)
    else:
        return func(x - y)

if a == 0:
    ans = func(b)
else:
    c, d =  func(a - 1), func(b)

    x = 0
    ans = 0
    while (1<<x) <= c or (1<<x) <= d:
        y, z = (c>>x)&1, (d>>x)&1
        if y ^ z == 1:
            ans += 1<<x
        x += 1

print(ans)
