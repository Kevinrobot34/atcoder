n = int(input())
c = [int(input()) for _ in range(n)]
c *= 2

offset = 0
while True:
    offset += 1
    if offset == n or c[offset - 1] != c[offset]:
        break

if offset == n:
    ans = -1
else:
    x = c[offset]
    m = 0
    l = 0
    for i in range(offset, n + offset):
        if c[i] == x:
            m += 1
        else:
            l = max(l, m)
            m = 1
            x = c[i]
    l = max(l, m)
    # print(offset, l)
    ans = (l + 1) // 2

print(ans)
