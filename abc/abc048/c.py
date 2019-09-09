n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    if a[i-1] + a[i] > x:
        ans += a[i-1] + a[i] - x
        if x >= a[i-1]:
            a[i] = x - a[i-1]
        else:
            a[i] = 0

print(ans)
