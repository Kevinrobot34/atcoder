n = int(input())
a = list(map(int, input().split()))
ans = s = r = 0
for l in range(n):
    while r < n and s < n:
        s += a[r]
        r += 1
    # `s = sum(a[l:r])` になってる
    if s == n:
        ans += 1
    s -= a[l]
print(ans)
