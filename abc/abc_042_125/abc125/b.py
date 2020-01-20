n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

p = []
for i in range(n):
    p.append(v[i] - c[i])

p.sort(reverse=True)
ans = 0
for i in range(n):
    if p[i] > 0:
        ans += p[i]
    else:
        break
print(ans)
