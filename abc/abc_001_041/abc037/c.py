n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
s = 0
for i in range(n):
    s += a[i]

    if i >= k - 1:
        ans += s
        s -= a[i-k+1]

print(ans)
