n = int(input())
ans = 0
x = 1
while int(str(x) * 2) <= n:
    ans += 1
    x += 1
print(ans)
