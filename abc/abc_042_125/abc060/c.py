n, t = map(int, input().split())
s = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    ans += min(t, s[i] - s[i-1])
ans += t

print(ans)
