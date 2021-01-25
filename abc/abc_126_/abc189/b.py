n, x = map(int, input().split())

ans = -1
s = 0
for i in range(n):
    v, p = map(int, input().split())
    s += v * p
    if s > x * 100 and ans == -1:
        ans = i + 1

print(ans)
