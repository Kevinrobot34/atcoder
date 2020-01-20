from heapq import heappush, heappop

n, m = map(int, input().split())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort(key=lambda x: (x[0], x[1]))
work.append([10**10, 0])
# print(work)

ans = 0
idx = 0
cand = []
for day in reversed(range(m+1)):
    while work[idx][0] <= m - day and idx < n:
        a, b = work[idx]
        heappush(cand, -b)
        idx += 1

    if len(cand) > 0:
        v = heappop(cand)
        ans += -v
        # print(day, -v)

print(ans)
