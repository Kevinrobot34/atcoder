from heapq import heappush, heappop, heapify

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
# print(p)
# print(q)
# print(r)

ar = p[:x]
ag = q[:y]
heapify(ar)
heapify(ag)

for i in range(c):
    if r[i] > ar[0] and r[i] > ag[0]:
        if ar[0] < ag[0]:
            heappop(ar)
            heappush(ar, r[i])
        else:
            heappop(ag)
            heappush(ag, r[i])
    elif r[i] <= ar[0] and r[i] > ag[0]:
        heappop(ag)
        heappush(ag, r[i])
    elif r[i] > ar[0] and r[i] <= ag[0]:
        heappop(ar)
        heappush(ar, r[i])
    else:
        # r[i] <= ar[0] and r[i] <= ag[0]
        break

# print(ar)
# print(ag)
ans = sum(ar) + sum(ag)
print(ans)
