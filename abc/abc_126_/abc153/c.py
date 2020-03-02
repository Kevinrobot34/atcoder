n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

if k == 0:
    ans = sum(h)
else:
    ans = sum(h[:-k])
print(ans)
