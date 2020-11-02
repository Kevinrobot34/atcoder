n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    ans += b * (b + 1) // 2
    ans -= a * (a - 1) // 2

print(ans)
