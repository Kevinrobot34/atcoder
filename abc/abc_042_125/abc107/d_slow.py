n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    for j in range(i + 1, n + 1):
        m = j - i
        b.append(a[i + m // 2])
b.sort()
print(b)
print(b[len(b) // 2])
