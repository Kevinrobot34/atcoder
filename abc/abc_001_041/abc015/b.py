n = int(input())
a = list(map(int, input().split()))

s = cnt = 0
for i in range(n):
    if a[i] > 0:
        cnt += 1
        s += a[i]

ans = (s + cnt - 1) // cnt
print(ans)
