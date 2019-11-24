n, k = map(int, input().split())
a = list(map(int, input().split()))
print([ai % k for ai in a])
ans = 0
for i in range(n):
    s = 0
    for j in range(n - i):
        s += a[i + j]
        if s % k == j + 1:
            print(i, i + j, j + 1)
            ans += 1

print(ans)
