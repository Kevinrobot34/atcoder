k, n = map(int, input().split())
a = list(map(int, input().split()))

a.append(k + a[0])
d = 0
for i in range(1, len(a)):
    d = max(a[i] - a[i - 1], d)

ans = k - d
print(ans)
