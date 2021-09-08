a, b = map(int, input().split())
c = a + b
if c >= 15 and b >= 8:
    ans = 1
elif c >= 10 and b >= 3:
    ans = 2
elif c >= 3:
    ans = 3
else:
    ans = 4
print(ans)
