import math
import sys
input = sys.stdin.readline

n = int(input())
th_list = []
seg = []
for _ in range(n):
    xi1, yi1, xi2, yi2 = map(int, input().split())
    thi1 = math.atan2(yi1, xi1)
    thi2 = math.atan2(yi2, xi2)
    if thi1 >= thi2:
        thi2 += math.pi * 2
