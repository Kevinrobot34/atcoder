n = int(input())
a = list(map(int, input().split()))

m = 0
ans = 0
for ai in a:
    if ai < m:
        ans += m - ai
    m = max(m, ai)

print(ans)
