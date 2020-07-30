from collections import deque
n = int(input())
a = [int(input()) for _ in range(n)]

a.sort()
a = deque(a)

b = deque([a.pop()])
