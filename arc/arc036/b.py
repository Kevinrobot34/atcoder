n = int(input())
h = [int(input()) for _ in range(n)]

ans = 0
s = u = 0
while s < n:
    while u + 1 < n and h[u] < h[u + 1]:
        u += 1
    while u + 1 < n and h[u] > h[u + 1]:
        u += 1
    ans = max(ans, u - s + 1)
    if s == u:
        s += 1
        u += 1
    else:
        s = u

print(ans)
