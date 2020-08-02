n, d = map(int, input().split())

ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x**2 + y**2 <= d**2:
        ans += 1
print(ans)
