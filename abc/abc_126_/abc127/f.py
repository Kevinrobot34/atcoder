from heapq import heappush, heappop
import sys
input = sys.stdin.readline

q = int(input())
a_sum = b_sum = 0
INF = 10**10
queue_l = [INF]
queue_r = [INF]
for i in range(q):
    s = input()
    if s[0] == '1':
        # update query
        _, a, b = map(int, s.split())

        ql_max = -queue_l[0]
        qr_min = queue_r[0]
        if a < ql_max:
            heappop(queue_l)
            heappush(queue_l, -a)
            heappush(queue_l, -a)
            heappush(queue_r, ql_max)
            a_sum += ql_max - a
        elif a > qr_min:
            heappop(queue_r)
            heappush(queue_r, a)
            heappush(queue_r, a)
            heappush(queue_l, -qr_min)
            a_sum += a - qr_min
        else:
            heappush(queue_l, -a)
            heappush(queue_r, a)

        b_sum += b
    else:
        # evaluation query
        ql_max = -queue_l[0]
        print(ql_max, a_sum + b_sum)
