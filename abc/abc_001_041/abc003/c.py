n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort(reverse=True)

ans = 0.0
for i in reversed(range(k)):
    ans = (ans + r[i]) / 2.0

print(ans)
