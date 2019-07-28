n, m = map(int, input().split())

ans = 0
if n == 1:
    if m == 1:
        ans = 1
    elif m >= 3:
        ans = m - 2
elif n >= 3 and m == 1:
    ans = n - 2
elif n >= 3 and m >= 3:
    ans = (n-2) * (m-2)

print(ans)
