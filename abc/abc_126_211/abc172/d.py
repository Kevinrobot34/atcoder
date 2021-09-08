n = int(input())

ans = n * (n + 1) // 2

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        ans += j

print(ans)
