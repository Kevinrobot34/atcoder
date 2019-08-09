from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

ans = 0
for x in d:
    cand = d[x]
    if x - 1 in d:
        cand += d[x - 1]
    if x + 1 in d:
        cand += d[x + 1]
    
    ans = max(ans, cand)

print(ans)
