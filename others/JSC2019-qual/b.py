n, k = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10**9 + 7

ans = 0
for i in range(n):
    x = 0
    for j in range(i+1, n):
        if a[i] > a[j]:
            x += 1
    y = 0
    for j in range(i):
        if a[i] > a[j]:
            y += 1

    ans += x * k * (k + 1) // 2
    ans %= MOD
    ans += y * (k-1) * k // 2
    ans %= MOD
    # print(i, x, y)

print(ans)
