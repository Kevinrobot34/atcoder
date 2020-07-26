import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
xyd = []
x_const_down = defaultdict(list)
x_const_up = defaultdict(list)

y_const_left = defaultdict(list)
y_const_right = defaultdict(list)

xmy_const_left = defaultdict(list)
xmy_const_down = defaultdict(list)

xpy_const_up = defaultdict(list)
xpy_const_left = defaultdict(list)

for _ in range(n):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    xyd.append((x, y, d))

    if d == 'U':
        x_const_up[x].append(y)
        xpy_const_up[x + y].append(x - y)
    elif d == 'D':
        x_const_down[x].append(y)
        xmy_const_down[x - y].append(x + y)
    elif d == 'L':
        y_const_left[y].append(x)
        xmy_const_left[x - y].append(x + y)
        xpy_const_left[x + y].append(x - y)
    else:  # d == 'R'
        y_const_right[y].append(x)

x_const_down = dict(x_const_down)
for i in x_const_down:
    x_const_down[i].append(float('inf'))
    x_const_down[i].sort()
x_const_up = dict(x_const_up)
for i in x_const_up:
    x_const_up[i].append(float('inf'))
    x_const_up[i].sort()
y_const_left = dict(y_const_left)
for i in y_const_left:
    y_const_left[i].append(float('inf'))
    y_const_left[i].sort()
y_const_right = dict(y_const_right)
for i in y_const_right:
    y_const_right[i].append(float('inf'))
    y_const_right[i].sort()

xmy_const_left = dict(xmy_const_left)
for i in xmy_const_left:
    xmy_const_left[i].append(float('inf'))
    xmy_const_left[i].sort()

xmy_const_down = dict(xmy_const_down)
for i in xmy_const_down:
    xmy_const_down[i].append(float('inf'))
    xmy_const_down[i].sort()

xpy_const_left = dict(xpy_const_left)
for i in xpy_const_left:
    xpy_const_left[i].append(float('inf'))
    xpy_const_left[i].sort()
xpy_const_up = dict(xpy_const_up)
for i in xpy_const_up:
    xpy_const_up[i].append(float('inf'))
    xpy_const_up[i].sort()

print(*xyd, sep='\n')

ans = float('inf')

# in x_const
for x, y, d in xyd:
    if d == 'U':
        if x in x_const_down:
            idx = bisect_left(x_const_down[x], y)
            ans = (x_const_down[x][idx] - y) // 2 * 10
        if x - y in xmy_const_left:
            idx = bisect_left(xmy_const_left[x - y], x + y)
            ans = (xmy_const_left[x - y][idx] - (x + y)) // 2 * 10
    elif d == 'D':
        if x + y in xpy_const_left:
            idx = bisect_left(xpy_const_left[x + y], x - y)
            ans = (xpy_const_left[x + y][idx] - (x - y)) // 2 * 10
    elif d == 'L':
        if y in y_const_right:
            idx = bisect_left(y_const_right[y], x)
            ans = (y_const_right[y][idx] - x) // 2 * 10
    else:  # d == 'R'
        if x - y in xmy_const_down:
            idx = bisect_left(xmy_const_down[x - y], x + y)
            ans = (xmy_const_down[x - y][idx] - (x + y)) // 2 * 10
        if x + y in xpy_const_up:
            idx = bisect_left(xpy_const_up[x + y], x - y)
            ans = (xpy_const_up[x + y][idx] - (x - y)) // 2 * 10
    print(x, y, d, idx, ans)

if ans == float('inf'):
    ans = 'SAFE'
print(ans)
