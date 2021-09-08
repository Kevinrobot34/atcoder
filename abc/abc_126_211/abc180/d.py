x, y, a, b = map(int, input().split())

ans = 0
while a * x - x <= b and a * x < y:
    x *= a
    ans += 1

ans += max(y - 1 - x, 0) // b

print(ans)
