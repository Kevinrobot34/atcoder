def f(x):
    ret = 0
    while x > 0:
        ret += x % 10
        x //= 10
    return ret


a, b = map(int, input().split())
ans = max(f(a), f(b))
print(ans)
