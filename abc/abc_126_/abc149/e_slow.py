n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(a)

b = []
c = []
for i in range(n):
    for j in range(n):
        b.append((a[i] + a[j], i, j))
        c.append(a[i] + a[j])
b.sort(reverse=True)
c.sort(reverse=True)
print(*b[:m], sep='\n')
cnt = [0] * n
for _, i, j in b[:m]:
    cnt[i] += 1
print(cnt)
print(sum(c[:m]))
