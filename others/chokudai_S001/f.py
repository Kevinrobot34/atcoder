n = int(input())
a = list(map(int, input().split()))
ans = 0
m = 0
for ai in a:
    if ai > m:
        ans += 1
    m = max(m, ai)
print(ans)
