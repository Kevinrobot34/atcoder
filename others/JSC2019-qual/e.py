from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, h, w = map(int, input().split())
info = []
row_pq = [[] for i in range(h)]
col_pq = [[] for i in range(w)]
for i in range(n):
    r, c, a = map(int, input().split())
    info.append((r-1, c-1, a))
    heappush(row_pq[r-1], (-a, i))
    heappush(col_pq[c-1], (-a, i))

cards = set()
ans = 0
for i in range(h):
    while row_pq[i]:
        a, idx = heappop(row_pq[i])
        a *= -1
        if len(col_pq[info[idx][1]]) == 1:
            continue
        else:
            a2, idx2 = heappop(row_pq[i])
            b, idx3 = heappop(col_pq[info[idx][1]])
            a2 *= -1
            b *= -1
            if b > a:
                # heappush(row_pq[info[idx2][0]], (-a2, idx2))
                heappush(col_pq[info[idx3][1]], (-b, idx3))
            elif b == a:
                b2, idx4 = heappop(col_pq[info[idx][1]])
                b2 *= -1
                if a2 > b2:
                    a, idx = a2, idx2
                else:
                    pass
                heappush(col_pq[info[idx3][1]], (-b, idx3))
                heappush(col_pq[info[idx3][1]], (-b2, idx4))



        if idx not in cards:
            cards.add(idx)
            print("row", i, a, idx)
            ans += a
            break

for j in range(w):
    while col_pq[j]:
        a, idx = heappop(col_pq[j])
        a *= -1
        if idx not in cards:
            cards.add(idx)
            ans += a
            print("col", j, a, idx)
            break

print(ans)
