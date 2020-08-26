from collections import defaultdict
from operator import itemgetter
import sys
input = sys.stdin.readline

h, w, m = map(int, input().split())
bombs = [tuple(map(int, input().split())) for _ in range(m)]

x_cnt = defaultdict(int)
y_cnt = defaultdict(int)
for x, y in bombs:
    x_cnt[x] += 1
    y_cnt[y] += 1

x_cnt_max = max(x_cnt.values())
y_cnt_max = max(y_cnt.values())
cnt = cnt_x = cnt_y = 0
for x, y in bombs:
    if x_cnt[x] == x_cnt_max and y_cnt[y] == y_cnt_max:
        cnt += 1

cnt_x = sum(v == x_cnt_max for v in x_cnt.values())
cnt_y = sum(v == y_cnt_max for v in y_cnt.values())
if cnt_x * cnt_y == cnt:
    ans = x_cnt_max + y_cnt_max - 1
else:
    ans = x_cnt_max + y_cnt_max

# print(cnt_x, cnt_y, cnt)
print(ans)
