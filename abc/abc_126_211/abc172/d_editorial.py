n = int(input())

ans = 0
for j in range(1, n + 1):
    m = n // j
    ans += j * m * (m + 1) // 2

print(ans)
