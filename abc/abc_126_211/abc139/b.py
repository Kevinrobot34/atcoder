a, b = map(int, input().split())

ans = 0

if b > a:
    b -= a
    ans = 1
    while b > 0:
        b -= a-1
        ans += 1
elif b > 1:
    ans = 1

print(ans)
