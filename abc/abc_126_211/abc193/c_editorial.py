n = int(input())
m = int(n**0.5) + 1
s = set()
for a in range(2, m):
    c = a**2
    while c <= n:
        s.add(c)
        c *= a
ans = n - len(s)
print(ans)
