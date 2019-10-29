a, b = map(int, input().split())

if 1 <= a <= 9 and 1 <= b <= 9:
    ans = a * b
else:
    ans = -1

print(ans)
