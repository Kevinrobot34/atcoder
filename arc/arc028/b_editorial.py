from heapq import heappop, heappush
n, k = map(int, input().split())
x = list(map(int, input().split()))
z = {x[i]: i for i in range(n)}

q = []
ans = []
for i in range(n):
    heappush(q, -x[i])
    if i >= k:
        _ = heappop(q)
    if i >= k - 1:
        ans.append(z[-q[0]] + 1)

print(*ans, sep='\n')
