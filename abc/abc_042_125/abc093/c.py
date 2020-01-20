d = list(map(int, input().split()))
a, b, c, = sorted(d)
sorted((a, b, c))

ans = (c - b) + (b - a) // 2
if (b - a) % 2 == 1:
    ans += 2

print(ans)
