from heapq import heappush, heappop

x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

pq = [(-a[0]-b[0]-c[0], 0, 0, 0)]
f = set()
for i in range(k):
    s, p, q, r = heappop(pq)
    print(-s)
    # print(-s, p, q, r, f)
    if p + 1 < x and (p+1, q, r) not in f:
        heappush(pq, (-a[p+1]-b[q]-c[r], p+1, q, r))
        f.add((p+1, q, r))
    if q + 1 < y and (p, q+1, r) not in f:
        heappush(pq, (-a[p]-b[q+1]-c[r], p, q+1, r))
        f.add((p, q+1, r))
    if r + 1 < z and (p, q, r+1) not in f:
        heappush(pq, (-a[p]-b[q]-c[r+1], p, q, r+1))
        f.add((p, q, r+1))
