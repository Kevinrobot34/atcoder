from collections import defaultdict
n = int(input())

d = defaultdict(int)
for i in range(1, n+1):
    j = 2
    while i > 1:
        if i % j == 0:
            d[j] += 1
            i = i // j
        else:
            j += 1

x = {75: 0, 25: 0, 15: 0, 5: 0, 3: 0}
for y in x:
    for v in d.values():
        if v + 1 >= y:
            x[y] += 1

ans = 0
ans += x[75]
ans += x[15] * (x[5] - 1) if x[5] >= 1 else 0
ans += x[25] * (x[3] - 1) if x[3] >= 1 else 0
ans += (x[5] * (x[5] - 1) // 2) * (x[3] - 2) if x[3] >= 2 else 0
print(ans)
