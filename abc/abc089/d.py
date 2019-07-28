import math
h, w, d = map(int, input().split())
a = [[0, 0] for i in range(h*w+1)]
for i in range(h):
    ai = list(map(int, input().split()))
    for j in range(w):
        a[ai[j]] = [i+1, j+1]

def dist(x, y):
    return abs(a[x][0] - a[y][0]) + abs(a[x][1] - a[y][1])

MAX_LOG = math.ceil(math.log2(h*w))
b = [[0 for j in range(MAX_LOG)] for i in range(h*w+1)]
for j in range(MAX_LOG):
    for i in range(1, h*w+1):
        if j == 0:
            b[i][j] = dist(i, i + d)
        else:
            b[i][j] = b[i][j-1] + b[i + d*(1<<j)][j-1]


q = int(input())
for _ in range(q):
    l, r = map(int, input())

print(a)
print(b)
