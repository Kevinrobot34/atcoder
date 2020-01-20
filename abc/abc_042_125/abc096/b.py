a, b, c = map(int, input().split())
k = int(input())

d = max(a, b, c)
ans = a + b + c - d
for i in range(k):
    d *= 2
ans += d

print(ans)
