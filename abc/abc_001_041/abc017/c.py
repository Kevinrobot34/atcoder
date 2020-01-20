import sys
input = sys.stdin.readline

n, m = map(int, input().split())
total = 0
jewel = [0] * (m + 1)
for i in range(n):
    l, r, s = map(int, input().split())
    l -= 1
    r -= 1
    jewel[l] += s
    jewel[r + 1] -= s
    total += s

jewel_min = total
for i in range(m):
    jewel[i + 1] += jewel[i]
    jewel_min = min(jewel[i], jewel_min)
ans = total - jewel_min

print(ans)
