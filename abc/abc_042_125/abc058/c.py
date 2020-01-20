from collections import defaultdict
n = int(input())

d = defaultdict(int)
si = input()
for j in range(len(si)):
    d[si[j]] += 1

for i in range(1, n):
    si = input()
    d2 = defaultdict(int)
    for j in range(len(si)):
        d2[si[j]] += 1

    for c in d:
        d[c] = min(d[c], d2[c])

ans = []
for c in sorted(list(d.keys())):
    for _ in range(d[c]):
        ans.append(c)
ans = ''.join(ans)

print(ans)
