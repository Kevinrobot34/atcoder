from collections import defaultdict
n, c = map(int, input().split())

tp = defaultdict(list)
i_max = 0
for _ in range(n):
    s, t, c = map(int, input().split())
    tp[c].append([s, t])
    i_max = max(i_max, t+1)

for c in tp:
    tp[c].sort()
    x = [tp[c][0]]
    for i in range(1, len(tp[c])):
        if x[-1][1] == tp[c][i][0]:
            x[-1][1] = tp[c][i][1]
        else:
            x.append(tp[c][i])
    tp[c] = x

r = [0] * (i_max + 5)

for c in tp:
    for s, t in tp[c]:
        r[s] += 1
        r[t+1] -= 1

ans = 0
for i in range(1, i_max+1):
    r[i] = r[i-1] + r[i]
    ans = max(ans, r[i])

print(ans)
