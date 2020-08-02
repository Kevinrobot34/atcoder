from collections import deque
n = int(input())
a = [int(input()) for _ in range(n)]

a.sort()
a = deque(a)

b = deque([a.pop()])

ans = 0
for _ in range(n - 1):
    x = max(
        abs(a[0] - b[0]),
        abs(a[0] - b[-1]),
        abs(a[-1] - b[0]),
        abs(a[-1] - b[-1]),
    )
    if x == abs(a[0] - b[0]):
        b.appendleft(a.popleft())
    elif x == abs(a[0] - b[-1]):
        b.append(a.popleft())
    elif x == abs(a[-1] - b[0]):
        b.appendleft(a.pop())
    else:  # x == abs(a[-1] - b[-1]):
        b.append(a.pop())
    ans += x

print(ans)
