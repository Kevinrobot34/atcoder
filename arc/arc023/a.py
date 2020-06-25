def func(y, m, d):
    if m == 1 or m == 2:
        y -= 1
        m += 12
    return 365 * y + y // 4 - y // 100 + y // 400 + (306 *
                                                     (m + 1)) // 10 + d - 429


y0 = int(input())
m0 = int(input())
d0 = int(input())

y1 = 2014
m1 = 5
d1 = 17

days1 = func(y1, m1, d1)
days0 = func(y0, m0, d0)
ans = days1 - days0
print(ans)
