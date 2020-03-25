from collections import deque
n = int(input())

d = deque(['a'])

while d:
    w = d.popleft()
    if len(w) == n:
        print(w)
    else:
        w_m = len(set(w))
        for i in range(w_m + 1):
            d.append(w + chr(ord('a') + i))
