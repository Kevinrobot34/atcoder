x0, y0 = map(int, input().split())
memo = {}


def func(y):
    if y in memo:
        return memo[y]

    if y == 1:
        ret = abs(x0 - y)
    elif y % 2 == 0:
        ret = min(abs(x0 - y), func(y // 2) + 1)
    else:
        ret = min(abs(x0 - y), func((y + 1) // 2) + 2, func((y - 1) // 2) + 2)

    memo[y] = ret
    return ret


ans = func(y0)
print(ans)
