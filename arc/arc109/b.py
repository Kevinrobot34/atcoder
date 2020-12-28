n = int(input())

m = 1
while (m + 1) * (m + 2) // 2 <= n + 1:
    m += 1

ans = n - m + 1
print(ans)
