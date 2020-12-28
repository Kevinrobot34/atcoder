a, b, x, y = map(int, input().split())
if a == b:
    ans = x
elif a < b:
    ans = x + (b - a) * min(x * 2, y)
else:
    ans = x + (a - b - 1) * min(x * 2, y)

print(ans)
