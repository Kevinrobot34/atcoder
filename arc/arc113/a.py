k = int(input())

ans = 0
for c in range(1, k + 1):
    for b in range(1, k // c + 1):
        ans += k // (b * c)
print(ans)
