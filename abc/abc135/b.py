n = int(input())
p = list(map(int, input().split()))

q = sorted(p)
a = 0
for i in range(n):
    if p[i] != q[i]:
        a += 1

if a <= 2:
    print("YES")
else:
    print("NO")
