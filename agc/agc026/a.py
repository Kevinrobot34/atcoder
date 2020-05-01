n = int(input())
a = list(map(int, input().split()))
a.append(0)

ans = 0
c = a[0]
cnt = 1
for i in range(1, n + 1):
    if a[i] != c:
        ans += cnt // 2
        c = a[i]
        cnt = 1
    else:
        cnt += 1

print(ans)
