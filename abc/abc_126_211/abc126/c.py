n, k = map(int, input().split())

ans = 0.0

p1 = min(k-1, n) / n
ans += 1.0 - p1

for i in range(1, min(k-1, n) + 1):
    p2 = 1.0 / n
    j = i
    while j < k:
        p2 *= 0.5
        j *= 2
    ans += p2

print(ans)
