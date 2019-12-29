n = int(input())

if n % 2 == 0:
    m = n // 2
    ans = 0
    while m > 0:
        ans += m // 5
        m //= 5
else:
    ans = 0

print(ans)
