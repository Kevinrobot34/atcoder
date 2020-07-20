import sys
input = sys.stdin.readline

n = int(input())
robots = [tuple(map(int, input().split())) for _ in range(n)]
robots.sort(key=(lambda robo: robo[0] + robo[1]))

z = -float('inf')
ans = 0
for x, l in robots:
    if z <= x - l:
        ans += 1
        z = x + l

print(ans)
