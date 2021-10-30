from heapq import heappop, heappush

q = int(input())

pq = []
x_base = 0

for _ in range(q):
    query = input()
    q0 = query[0]
    if q0 == '1':
        _, xi = map(int, query.split())
        heappush(pq, xi - x_base)
    elif q0 == '2':
        _, xi = map(int, query.split())
        x_base += xi
    else:
        ans = x_base + heappop(pq)
        print(ans)
