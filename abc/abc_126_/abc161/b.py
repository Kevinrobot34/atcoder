n, m = map(int, input().split())
a = list(map(int, input().split()))

b = sum(a) / (4.0 * m)
cnt = 0
for ai in a:
    if ai >= b:
        cnt += 1
ans = 'Yes' if cnt >= m else 'No'
print(ans)
