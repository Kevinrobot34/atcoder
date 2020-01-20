a, b = map(int, input().split())

c1 = '#' if a < b else '.'
c2 = '.' if a < b else '#'

ans = []

WIDTH = 50
d = abs(a - b)
d1 = d % WIDTH
d2 = d // WIDTH
e = min(a, b) - 1
f = e % WIDTH
e = e // WIDTH
ans.append(c1*WIDTH*2)
ans.append((c2+c1)*f + c1 * 2 * (WIDTH - f))
ans.append(c1*WIDTH*2)
for i in range(e+1):
    if i % 2 == 0:
        ans.append((c1+c2)*WIDTH)
    else:
        ans.append((c2+c1)*WIDTH)
ans.append(c2*WIDTH*2)
ans.append((c1+c2)*f + c2 * 2 * (WIDTH-f))
ans.append(c2*WIDTH*2)

if d1 != 0:
    ans.append((c2+c1)*d1 + c2 * 2 * (WIDTH - d1))
    ans.append(c2*WIDTH*2)
for i in range(d2):
    ans.append((c2+c1)*WIDTH)
    ans.append(c2*WIDTH*2)


print(len(ans), WIDTH*2)
for ansi in ans:
    print(ansi)
