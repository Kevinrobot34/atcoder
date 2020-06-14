a, b, m = map(int, input().split())
pa = list(map(int, input().split()))
pb = list(map(int, input().split()))

ans = min(pa) + min(pb)
for _ in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    ans = min(ans, pa[x] + pb[y] - c)

print(ans)
