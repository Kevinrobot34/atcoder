n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    m = a[i]
    for j in range(i + 1, n + 1):
        ans = max(ans, m * (j - i))
        if j != n:
            m = min(m, a[j])
print(ans)
