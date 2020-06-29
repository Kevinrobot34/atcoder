from heapq import heappush, heappop

k = int(input())
n = int(input())

house = []
d = []
for i in range(n):
    ai, di = map(int, input().split())
    heappush(house, (ai, i))
    d.append(di)

ans = 0
for _ in range(k):
    ai, i = heappop(house)
    ans += ai
    heappush(house, (ai + d[i], i))

print(ans)
