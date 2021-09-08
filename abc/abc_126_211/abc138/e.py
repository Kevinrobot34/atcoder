from collections import defaultdict
s = input()
t = input()

ds = defaultdict(int)
for i in range(len(s)):
    ds[s[i]] += 1
dt = defaultdict(int)
for i in range(len(t)):
    dt[t[i]] += 1

possible = True
for ti in dt:
    if ti not in ds:
        possible = False
        break

if possible:
    n = len(s)
    pos = defaultdict(list)
    for i in range(n*2):
        pos[s[i%n]].append(i)

    edge = defaultdict(list)
    for c in pos:
        x = 0
        for i in range(n):
            if i >= pos[c][x]:
                x += 1
            edge[c].append(pos[c][x])

    # print(pos)
    # print(edge)
    ans = 0
    x = 0
    for i in range(n):
        if s[i] == t[0]:
            ans = i + 1
            x = i
            break

    # print(ans)
    for i in range(1, len(t)):
        ans += edge[t[i]][x%n] - x
        x = edge[t[i]][x%n] % n
        # print(ans, t[i])

else:
    ans = -1

print(ans)
