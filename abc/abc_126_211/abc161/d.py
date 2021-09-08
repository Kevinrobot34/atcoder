from collections import deque
k = int(input())

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for _ in range(k):
    ans = x = q.popleft()
    x0 = x % 10
    if x0 >= 1:
        q.append(x * 10 + x0 - 1)
    q.append(x * 10 + x0)
    if x0 <= 8:
        q.append(x * 10 + x0 + 1)

print(ans)
