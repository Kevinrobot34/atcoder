n = int(input())
a = list(map(int, input().split()))

s = sum(a)
s1 = 0
ans = 10**15
for i in range(n-1):
    s1 += a[i]
    ans = min(ans, abs(s1 - (s-s1)))

print(ans)
