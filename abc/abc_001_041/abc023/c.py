from collections import Counter
r, c, k = map(int, input().split())
n = int(input())
row = [0] * r
col = [0] * c
candy = []
for i in range(n):
    ri, ci = map(int, input().split())
    ri -= 1
    ci -= 1
    candy.append((ri, ci))
    row[ri] += 1
    col[ci] += 1

cnt_row = dict(Counter(row))
cnt_col = dict(Counter(col))

ans = 0
for r in cnt_row:
    if k - r in cnt_col:
        ans += cnt_row[r] * cnt_col[k - r]

for r, c in candy:
    if row[r] + col[c] == k:
        ans -= 1
    elif row[r] + col[c] == k + 1:
        ans += 1

print(ans)
