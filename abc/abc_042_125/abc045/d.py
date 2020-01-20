from collections import defaultdict
import sys
input = sys.stdin.readline

h, w, n = map(int, input().split())
d = defaultdict(int)
dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
for i in range(n):
    a, b = map(int, input().split())
    for k in range(9):
        d[(a+dx[k], b+dy[k])] += 1

ans = [0] * 10
for a, b in d:
    if a <= 1 or b <= 1 or a > h-1 or b > w-1:
        continue
    ans[d[(a, b)]] += 1
ans[0] = (h-2) * (w-2) - sum(ans)

for ans_i in ans:
    print(ans_i)
