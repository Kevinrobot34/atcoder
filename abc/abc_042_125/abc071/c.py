from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for ai in a:
    d[ai] += 1

cand = [k for k, v in d.items() if v >= 2]
cand.sort()

ans = 0
if len(cand) >= 1 and d[cand[-1]] >= 4:
    ans = cand[-1] ** 2
elif len(cand) >= 2:
    ans = cand[-1] * cand[-2]

print(ans)
