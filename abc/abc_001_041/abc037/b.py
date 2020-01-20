n, q = map(int, input().split())
a = [0] * n
for i in range(q):
    l, r, t = map(int, input().split())
    l, r = l - 1, r - 1
    for j in range(l, r + 1):
        a[j] = t
print(*a, sep='\n')
