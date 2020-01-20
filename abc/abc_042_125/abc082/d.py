from collections import defaultdict
s = input() + 'T'
x, y = map(int, input().split())

si = 0
while s[si] == 'F':
    x -= 1
    si += 1
si += 1

d = [[], []]
dir = 1
z = 0
for i in range(si, len(s)):
    if s[i] == 'T':
        if z > 0:
            d[dir].append(z)
        dir = (dir + 1) % 2
        z = 0
    else:
        z += 1

d[0].sort()
d[1].sort()

def check(a, b):
    c1 = defaultdict(int)
    c2 = defaultdict(int)
    c1[0] += 1
    for i in range(len(a)):
        for c in c1:
            c2[c+a[i]] += 1
            c2[c-a[i]] += 1
        c1 = c2.copy()
        c2 = defaultdict(int)

    # print(c1.keys())
    return (b in c1)

if check(d[0], x) and check(d[1], y):
    print("Yes")
else:
    print("No")
