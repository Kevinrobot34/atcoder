x = int(input())

ans = (x // 11) * 2
x = x % 11
if 0 < x <= 6:
    ans += 1
elif 6 < x:
    ans += 2

print(ans)
