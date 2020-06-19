from itertools import permutations
n = int(input())
t = [int(input()) for _ in range(n)]
s = sum(t)
m = min(2, n)

ans = min([max(t[i], s - t[i]) for i in range(n)])
for p in permutations(range(n), r=m):
    s2 = sum([t[i] for i in p])
    cand = max(s - s2, s2)
    ans = min(ans, cand)
print(ans)
