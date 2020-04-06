n, s, t = map(int, input().split())

w = int(input())
ans = 1 if s <= w <= t else 0
for _ in range(1, n):
    a = int(input())
    w += a
    if s <= w <= t:
        ans += 1

print(ans)
