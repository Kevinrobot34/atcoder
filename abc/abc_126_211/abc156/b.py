n, k = map(int, input().split())
ans = 0
while k**ans <= n:
    ans += 1
print(ans)
