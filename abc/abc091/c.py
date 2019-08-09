from collections import defaultdict
from heapq import heappush, heappop
n = int(input())
red = [list(map(int, input().split())) for i in range(n)]
blue = [list(map(int, input().split())) for i in range(n)]

a = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if red[i][0] < blue[j][0] and res[i][1] < blue[j][1]:
            a[i].append(j)
