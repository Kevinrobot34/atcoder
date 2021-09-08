from heapq import heappush, heappop
import sys
input = sys.stdin.readline

h, w, k = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
c_ = [tuple(input()) for _ in range(h)]
c = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if c_[i][j] == '@':
            c[i][j] = True
# print(x1, y1)
# print(x2, y2)

dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]
MAX = 10**7


def convert(x, y, d):
    return (x * w + y) * 4 + d


# dp = [[[(MAX, MAX)] * 4 for _ in range(w)] for _ in range(h)]
dp = [MAX * (k + 1) + k] * (h * w * 4)

# q = [((1, 0, x1, y1, i)) for i in range(4)]
q = [((k + 1, convert(x1, y1, i))) for i in range(4)]

while q:
    c0, xyd = heappop(q)
    c1 = c0 // (k + 1)
    c2 = c0 % (k + 1)
    # print(x, y, d, c1, c2)
    d = xyd % 4
    y = (xyd // 4) % w
    x = (xyd // 4) // w
    if c1 > dp[xyd] // (k + 1):
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nxyi = convert(nx, ny, i)
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if c[nx][ny]:
            continue
        if i == d and c2 < k:
            if dp[nxyi] > c1 * (k + 1) + c2 + 1:
                dp[nxyi] = c1 * (k + 1) + c2 + 1
                heappush(q, (dp[nxyi], nxyi))
        else:
            if dp[nxyi] > (c1 + 1) * (k + 1) + 1:
                dp[nxyi] = (c1 + 1) * (k + 1) + 1
                heappush(q, (dp[nxyi], nxyi))

ans = min(dp[convert(x2, y2, i)] // (k + 1) for i in range(4))
if ans == MAX:
    ans = -1
print(ans)
