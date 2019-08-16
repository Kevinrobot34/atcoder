n, m = map(int, input().split())

l_max, r_min = 0, n
for i in range(m):
    l, r = map(int, input().split())
    l_max = max(l, l_max)
    r_min = min(r, r_min)

ans = max(0, r_min - l_max + 1)
print(ans)
