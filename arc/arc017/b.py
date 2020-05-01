n, k = map(int, input().split())
a = list(int(input()) for _ in range(n))
a.append(0)

ans = 0
c = 0
for i in range(n):
    if a[i - 1] < a[i]:
        c += 1
    else:
        c = 1
    if c >= k:
        ans += 1
print(ans)
