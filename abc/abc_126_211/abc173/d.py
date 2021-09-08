n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = a[0]
m = n - 2
for i in range(1, n):
    if m > 1:
        ans += a[i] * 2
        m -= 2
    elif m == 1:
        ans += a[i]
        m -= 1
    else:
        break

    if m == 0:
        break

print(ans)
