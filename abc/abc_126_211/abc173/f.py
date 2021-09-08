n = int(input())

ans = 0
for i in range(1, n + 1):
    ans += i * (i + 1) // 2

for _ in range(n - 1):
    u, v = map(int, input().split())
    if v < u:
        u, v = v, u
    ans -= u * (n - v + 1)

print(ans)
