a = list(map(int, input().split()))

b = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            b.append(a[i] + a[j] + a[k])

b.sort()

print(b[-3])
