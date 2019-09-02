from collections import deque
n = int(input())
a = list(map(int, input().split()))

dq = deque([])
for i in range(n):
    if (i + n) % 2 == 0:
        dq.append(str(a[i]))
    else:
        dq.appendleft(str(a[i]))

print(' '.join(dq))
