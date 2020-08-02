n, m, d = map(int, input().split())

if d > 0:
    ans = 2 * (n - d) / (n**2) * (m - 1)
else:
    ans = (n - d) / (n**2) * (m - 1)
print(ans)
