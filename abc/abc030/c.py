from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ctime = 0
ans = 0
while True:
    idx = bisect_left(a, ctime)
    if idx == n:
        break
    ctime = a[idx] + x

    idx = bisect_left(b, ctime)
    if idx == m:
        break
    ctime = b[idx] + y

    ans += 1

print(ans)
