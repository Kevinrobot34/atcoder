n, a, b = map(int, input().split())
s = [int(input()) for _ in range(n)]

b0 = max(s) - min(s)
a0 = sum(s) / n

if b0 != 0:
    p = b / b0
    q = a - p * a0
    print(p, q)
else:
    print(-1)
