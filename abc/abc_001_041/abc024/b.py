n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n - 1):
    ans += min(a[i + 1], a[i] + t) - a[i]
ans += t

print(ans)
