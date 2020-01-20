from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

b = defaultdict(int)
for i in range(n):
    b[a[i]] += 1

ans = 0
for k in b:
    if b[k] >= k:
        ans += b[k] - k
    else:
        ans += b[k]

print(ans)
