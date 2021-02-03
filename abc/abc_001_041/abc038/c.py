n = int(input())
a = list(map(int, input().split()))
a.append(0)
ans = 0
r = 1
for l in range(n):
    while r < n and a[r - 1] < a[r]:
        r += 1

    ans += r - l

    if l + 1 == r:
        r += 1

print(ans)
