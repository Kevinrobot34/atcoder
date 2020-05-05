k = int(input())

k1 = k // 50
k2 = k % 50

n = 50
a = list(range(n))[::-1]
for i in range(n):
    a[i] += k1
for i in range(k2):
    a[i] += 1

print(n)
print(*a)
