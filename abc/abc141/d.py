from heapq import heappush, heappop

n, m = map(int, input().split())
a = list(map(int, input().split()))

pq = []
for i in range(n):
    heappush(pq, -a[i])

for i in range(m):
    a_max = - heappop(pq)
    if a_max == 0:
        break
    a_max //= 2
    heappush(pq, -a_max)

ans = -sum(pq)
print(ans)
