from collections import defaultdict, deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)

x = []
for i in range(1, s+1):
    if i * i > s:
        break
    if s % i == 0:
        x.append(i)
        x.append(s//i)

ans = 0
for xi in x:
    b = []
    for i in range(n):
        if a[i] % xi != 0:
            b.append(a[i] % xi)
    b.sort()
    b = deque(b)

    c = 0
    r = 0
    while b:
        q = b.pop() + r

        while q < xi:
            p = b.popleft()
            q += p
            c += p

        r = q - xi

    if c <= k:
        ans = max(ans, xi)

print(ans)
