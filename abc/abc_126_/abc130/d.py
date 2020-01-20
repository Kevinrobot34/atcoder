n, k = map(int, input().split())
a = list(map(int, input().split()))

l = r = 0
ans = 0
s = 0
while l < n:
    while s < k and r < n:
        s += a[r]
        r += 1

    if s >= k:
        ans += n - r + 1

    s -= a[l]
    l += 1

print(ans)
