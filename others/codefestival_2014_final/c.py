def func(n):
    base = n
    x = 1
    res = 0
    while n:
        res += x * (n % 10)
        x *= base
        n //= 10
    return res


a = int(input())

k = 10
ans = -1
while True:
    y = func(k)
    if y > a:
        break
    elif y == a:
        ans = k
    k += 1

print(ans)
