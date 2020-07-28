a, b = map(int, input().split())
if a + b == 15:
    ans = '+'
elif a * b == 15:
    ans = '*'
else:
    ans = 'x'
print(ans)
