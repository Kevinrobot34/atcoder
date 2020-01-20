n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    ans += min((x[i] - x[i-1]) * a, b)

print(ans)
