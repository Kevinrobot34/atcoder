from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

b = defaultdict(int)
for i in range(n):
    b[a[i]] += 1

c = list(b.values())
c.sort()

ans = 0
for i in range(len(c) - k):
    ans += c[i]

print(ans)
