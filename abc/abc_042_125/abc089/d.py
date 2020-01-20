import math
import sys
input = sys.stdin.readline

h, w, d = map(int, input().split())
a = [[0, 0] for i in range(h*w+1)]
for i in range(h):
    ai = list(map(int, input().split()))
    for j in range(w):
        a[ai[j]] = [i+1, j+1]

def dist(p1, p2):
    return abs(a[p1][0] - a[p2][0]) + abs(a[p1][1] - a[p2][1])

MAX_LOG = math.ceil(math.log2(h*w))
# MAX_LOG = 18
b = [[0 for j in range(MAX_LOG)] for i in range(h*w+1)]
for j in range(MAX_LOG):
    for i in range(1, h*w+1):
        if j == 0:
            if i + d < h*w + 1:
                b[i][j] = dist(i, i + d)
        elif i + d*(1<<j) < h*w + 1:
            b[i][j] = b[i][j-1] + b[i + d*(1<<(j-1))][j-1]

# for bi in b:
#     print(bi)

def query(l, bit):
    if bit == 0:
        return 0
    j = 0
    while (bit>>j) & 1 == 0:
        j += 1

    return b[l][j] + query(l + d * (1<<j), bit ^ (1<<j))


q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(query(l, (r-l)//d))
