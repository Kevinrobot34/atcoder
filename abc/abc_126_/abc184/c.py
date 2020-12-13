a, b = map(int, input().split())
c, d = map(int, input().split())

if abs(a - c) + abs(b - d) <= 3:
    ans = 1
else:
    if abs((a + b) - (c + d)) == 0:
        ans = 1
    elif abs((a - b) - (c - d)) == 0:
        ans = 1
    elif abs(a - c) + abs(b - d) <= 6:
        ans = 2
    elif abs((a + b) - (c + d)) <= 3:
        ans = 2
    elif abs((a - b) - (c - d)) <= 3:
        ans = 2
    elif
    else:
        ans = 3

print(ans)
