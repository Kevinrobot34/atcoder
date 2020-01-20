w, a, b = map(int, input().split())

if a <= b <= a + w:
    ans = 0
else:
    ans = min(abs(b - a), abs(b - a - w), abs(b + w - a))

print(ans)
