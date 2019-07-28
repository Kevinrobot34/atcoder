from collections import defaultdict
n = int(input())
ds = defaultdict(int)
for i in range(n):
    s = input()
    ds[s] += 1


m = int(input())
for i in range(m):
    t = input()
    ds[t] -= 1

print(max(max(ds.values()), 0))
