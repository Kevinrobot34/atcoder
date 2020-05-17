p = float(input())


def func(t):
    return t + p * 2**(-t / 1.5)


left = 0.0
right = p
while right - left > 1e-8:
    c1 = (2 * left + right) / 3
    c2 = (left + 2 * right) / 3
    if func(c1) < func(c2):
        right = c2
    else:
        left = c1

ans = func(left)
print(ans)
