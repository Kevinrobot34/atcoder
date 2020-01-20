from collections import defaultdict
from heapq import heappush, heappop

n = int(input())
red = [list(map(int, input().split())) for i in range(n)]
blue = [list(map(int, input().split())) for i in range(n)]
blue.sort()
# print(blue)

red_flag = [0] * n
ans = 0
for i in range(n):
    idx = -1
    for j in range(n):
        if red[j][0] >= blue[i][0] or red[j][1] >= blue[i][1] or red_flag[j] == 1:
            continue
        if idx == -1 or red[idx][1] < red[j][1]:
            idx = j

    if idx >= 0:
        red_flag[idx] = 1
        ans += 1

print(ans)
