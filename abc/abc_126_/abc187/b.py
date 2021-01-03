n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    xi, yi = p[i]
    for j in range(i):
        xj, yj = p[j]
        if abs(yj - yi) <= abs(xj - xi):
            ans += 1

print(ans)
