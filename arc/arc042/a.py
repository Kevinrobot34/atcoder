n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
a = a[::-1]

ans = []
s = set()
for i in range(m):
    if a[i] not in s:
        ans.append(a[i])
        s.add(a[i])

for i in range(1, n + 1):
    if i not in s:
        ans.append(i)

print(*ans, sep='\n')
