n = int(input())
norm = [tuple(map(int, input().split())) for _ in range(n)]


def func_x(x):
    ret = 0.0
    for xi, yi, ci in norm:
        ret = max(ret, ci * abs(xi - x))
    return ret


def func_y(y):
    ret = 0.0
    for xi, yi, ci in norm:
        ret = max(ret, ci * abs(yi - y))
    return ret


def ternary_search(f, left, right, EPS):
    while right - left > EPS:
        c1 = (2 * left + right) / 3
        c2 = (left + 2 * right) / 3
        if f(c1) < f(c2):
            right = c2
        else:
            left = c1
    return left


x = ternary_search(func_x, -2 * 10**5, 2 * 10**5, 1e-8)
y = ternary_search(func_y, -2 * 10**5, 2 * 10**5, 1e-8)

ans = max(func_x(x), func_y(y))
print(ans)
