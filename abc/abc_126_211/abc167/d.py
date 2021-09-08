n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

loop = [0]
s = {0}
while a[loop[-1]] not in s:
    s.add(a[loop[-1]])
    loop.append(a[loop[-1]])

idx = loop.index(a[loop[-1]])
# print(idx, loop)

if k < len(loop):
    ans = loop[k] + 1
else:
    ans = loop[(k - idx) % (len(loop) - idx) + idx] + 1
print(ans)
