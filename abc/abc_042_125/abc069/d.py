h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    for j in range(a[i]):
        b.append(i + 1)

ans = []
for i in range(0, h*w, w):
    if (i // w) % 2 == 0:
        ans.append(b[i:i+w])
    else:
        ans.append(list(reversed(b[i:i+w])))

print('\n'.join([' '.join([str(aij) for aij in ai]) for ai in ans]))
