x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = []
for i in range(x):
    for j in range(y):
        d.append(a[i] + b[j])
d.sort(reverse=True)

e = []
for i in range(min(len(d), k)):
    for j in range(z):
        e.append(d[i] + c[j])
e.sort(reverse=True)

for i in range(k):
    print(e[i])
