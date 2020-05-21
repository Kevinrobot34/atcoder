a, b = map(int, input().split())
if a > 0 or b < 0:
    ans = b - a
else:
    ans = b - a - 1
print(ans)
