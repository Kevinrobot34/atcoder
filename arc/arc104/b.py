from collections import Counter
n, s = input().split()
n = int(n)

d = {'A': (0, +1), 'T': (0, -1), 'G': (+1, 0), 'C': (-1, 0)}

cs = [(0, 0)] * (n + 1)
for i in range(n):
    a1, b1 = cs[i]
    a2, b2 = d[s[i]]
    cs[i + 1] = (a1 + a2, b1 + b2)

cnt = Counter(cs)
ans = sum(m * (m - 1) // 2 for m in cnt.values())
print(ans)
