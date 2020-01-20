from collections import defaultdict

n, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]

gg = [defaultdict(int) for _ in range(3)]
for i in range(n):
    g = list(map(int, input().split()))
    for j in range(n):
        gg[(i+j)%3][g[j]-1] += 1

ans = max(max(d)) * n**2
for c0 in range(c):
    for c1 in range(c):
        if c1 == c0:
            continue
        for c2 in range(c):
            if c0 == c2 or c1 == c2:
                continue

            tmp_ans = sum([d[i][c0] * gg[0][i] for i in gg[0]]) \
                    + sum([d[i][c1] * gg[1][i]  for i in gg[1]]) \
                    + sum([d[i][c2] * gg[2][i]  for i in gg[2]])
            # print(c0, c1, c2, tmp_ans)
            ans = min(ans, tmp_ans)

print(ans)
