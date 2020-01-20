n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    while a[i] % 2 == 0:
        ans += 1
        a[i] = a[i] // 2

print(ans)
