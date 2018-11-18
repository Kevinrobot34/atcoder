h, w = map(int, input().split())
n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(str(input()))

ans = 0

left = m
right = -1
for i in range(min(n, h-n)):
    for l in range(m):
        if l == left:
            break
        if a[i][l] == '#':
            left = l
            break
    for r in reversed(range(m)):
        if r == right:
            break
        if a[i][r] == '#':
            right = r
            break

    if left != m:
        if w >= 2*m:
            ans += w - l - (m-1-r)
            #print(i, w - l - (m-1-r))
        #else
#print(ans)

if h >= 2*n and left != m:
    ans +=  (w - l - (m-1-r)) * (h - 2*n)
#print(ans)

left = m
right = -1
for i in reversed(range(n)):
    for l in range(m):
        if l == left:
            break
        if a[i][l] == '#':
            left = l
            break
    for r in reversed(range(m)):
        if r == right:
            break
        if a[i][r] == '#':
            right = r
            break

    if left != m:
        ans += w - l - (m-1-r)
        #print(i, w - l - (m-1-r))

print(ans)
