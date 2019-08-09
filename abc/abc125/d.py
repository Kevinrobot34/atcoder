n = int(input())
a = list(map(int, input().split()))

b = []
m = 0
for i in range(n):
    if a[i] < 0:
        m += 1
    b.append(abs(a[i]))

b.sort()
ans = sum(b)
if m % 2 == 1:
    ans -= b[0] * 2

print(ans)
