from heapq import heappush, heappop
n = int(input())
a = list(map(int, input().split()))

s1 = [0] * 3*n
pq = []
s = 0
for i in range(3*n):
    if len(pq) < n:
        s += a[i]
        heappush(pq, a[i])
        if len(pq) == n:
            s1[i] = s
    else:
        s += a[i]
        heappush(pq, a[i])
        s -= heappop(pq)
        s1[i] = s


s2 = [0] * 3*n
pq = []
s = 0
for i in reversed(range(3*n)):
    if len(pq) < n:
        s += a[i]
        heappush(pq, -a[i])
        if len(pq) == n:
            s2[i] = s
    else:
        s += a[i]
        heappush(pq, -a[i])
        s -= -heappop(pq)
        s2[i] = s

ans = - 10**15
for i in range(n-1, 2*n):
    ans = max(ans, s1[i] - s2[i+1])
print(ans)
