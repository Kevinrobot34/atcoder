n, a, b = map(int, input().split())

if n == 1 and a != b:
    ans = 0
elif b < a:
    ans = 0
else:
    ans = (b * (n - 1) + a) - (a * (n - 1) + b) + 1

print(ans)
